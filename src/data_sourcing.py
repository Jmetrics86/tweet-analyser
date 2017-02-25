# -*- coding: utf-8 -*-

import json

from tweepy import Cursor, RateLimitError, TweepError


def get_user(twitter_connection):
    """get user id from input username"""

    username = ""

    while not username:
        username = input("Please enter the twitter screen_name: ")

    user = twitter_connection.get_user(username)
    return user.id


def get_hashtag():
    """get hashtag to search from user input"""

    hashtag = ""
    while not hashtag:
        hashtag = input("Please enter the hashtag to search with: ")

    if hashtag[0] != '#':
        hashtag = "#" + str(hashtag)
    else:
        pass

    return hashtag


def process_or_store(tweet, store):
    """process or store tweet data"""
    store.append(json.dumps(tweet, indent=4))


def analysis_decider():
    """Takes analysis choice from user"""

    source_choice = 0
    while source_choice not in [1, 2]:
        source_choice = int(input("Would you like to analyse the user timeline(1) or search for a term(2)?\n"))

        if source_choice not in [1, 2]:
            print("Error! Acceptable inputs are 1 (timeline) or 2 (term)")

    return source_choice


def rate_error():
    print("Error! Twitter rate limit reach. Wait 15 mins and try again.")


def tweepy_sourcing_error():
    print("Error! Unable to retrieve tweets.")


def get_timeline(twitter_connection, user_id):
    """Reads specified user_timeline and returns a list of tweets"""

    json_store = []
    try:
        for status in Cursor(twitter_connection.user_timeline, id=user_id).items():
            process_or_store(status._json, json_store)
    except RateLimitError:
        rate_error()
    except TweepError:
        tweepy_sourcing_error()

    return json_store


def search_hashtag(twitter_connection, hashtag):
    """Searches for specified hashtag and returns a list of tweets"""

    json_store = []
    try:
        for status in Cursor(twitter_connection.search, q=hashtag).items():
            process_or_store(status._json, json_store)
    except RateLimitError:
        rate_error()
    except TweepError:
        tweepy_sourcing_error()

    return json_store


def data_router(source_choice, api_connection):
    """Routes analysis choice to relevant Cursor query method and passes back the list of tweets"""

    if source_choice == 1:
        user_id = get_user(api_connection)
        tweets = get_timeline(api_connection, user_id)

    elif source_choice == 2:
        hashtag = get_hashtag()
        tweets = search_hashtag(api_connection, hashtag)

    else:
        tweets = []

    return tweets
