# -*- coding: utf-8 -*-

import json
from tweepy import Cursor, RateLimitError


def get_user(twitter_connection):
    """get user id from username"""
    username = input("Please enter the twitter screen_name: ")
    user = twitter_connection.get_user(username)
    return user.id


def get_hashtag():
    """get hashtag to search"""
    hashtag = input("Please enter the hashtag to search with: ")

    while not hashtag:
        print("Error! Hashtag cannot be empty.")
        get_hashtag()

    if hashtag[0] != '#':
        hashtag = '#'.append(hashtag)
    else:
        pass

    return hashtag


def process_or_store(tweet, store):
    """process or store tweet data"""
    store.append(json.dumps(tweet, indent=4))


def analysis_decider():
    source_choice = input("Would you like to analyse the user timeline(1) or search for a term(2)?")
    while source_choice not in [1,2]:
        print("Error! Acceptable inputs are 1 (timeline) or 2 (term)")
        analysis_decider()
    return source_choice


def get_timeline(twitter_connection, user_id):
    json_store = []
    try:
        for status in Cursor(twitter_connection.user_timeline, id=user_id).items():
            process_or_store(status._json, json_store)
    except RateLimitError:
        print("Error! Twitter rate limit reach. Wait 15 mins and try again.")
    return


def search_for_hashtag(twitter_connection, hashtag):
    json_store = []
    try:
        for status in Cursor(twitter_connection.search, q=hashtag).items():
            process_or_store(status._json, json_store)
    except RateLimitError:
        print("Error! Twitter rate limit reach. Wait 15 mins and try again.")
    return


def analysis_router(source_choice, api_connection):
    if source_choice == 1:
        user_id = get_user(api_connection)
        get_timeline(api_connection, user_id)
    elif source_choice == 2:
        hashtag = get_hashtag()
        search_for_hashtag(api_connection, hashtag)
    else:
        print("Error! Unacceptable analysis choice passed. Please re-enter.")
        analysis_decider()
    return
