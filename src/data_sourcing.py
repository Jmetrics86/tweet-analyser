# -*- coding: utf-8 -*-

import json

from tweepy import Cursor, RateLimitError


def get_user(twitter_connection):
    """get user id from username"""
    username = input("Please enter the twitter screen_name: ")
    user = twitter_connection.get_user(username)
    return user.id


def process_or_store(tweet, store):
    """process or store tweet data"""
    store.append(json.dumps(tweet, indent=4))


def get_timeline(twitter_connection, user_id):
    json_store = []
    try:
        for status in Cursor(twitter_connection.user_timeline, id=user_id).items():
            process_or_store(status._json, json_store)
    except RateLimitError:
        print("Error! Twitter rate limit reach. Wait 15 mins and try again.")


def search_term(twitter_connection, hashtag):
    json_store = []
    try:
        for status in Cursor(twitter_connection.search, q=hashtag).items():
            process_or_store(status._json, json_store)
    except RateLimitError:
        print("Error! Twitter rate limit reach. Wait 15 mins and try again.")
