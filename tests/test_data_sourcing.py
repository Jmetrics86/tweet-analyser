# -*- coding: utf-8 -*-

import unittest.mock

from data_sourcing import *
from utils.ConfigReader import ConfigReader
from utils.TwitterAuthenticate import TwitterAuthenticate


def test_get_user():
    config = ConfigReader('resources/credentials.properties')

    twitter_connection = TwitterAuthenticate(config.consumer_key, config.consumer_secret,
                                             config.access_token_key, config.access_token_secret
                                             ).request_auth().make_connection()

    with unittest.mock.patch('builtins.input', return_value='jhole89'):
        assert get_user(twitter_connection) == 3291780214


def test_get_hashtag():
    with unittest.mock.patch('builtins.input', return_value='#TestHashtag'):
        assert get_hashtag() == '#TestHashtag'
    with unittest.mock.patch('builtins.input', return_value='TestHashtag'):
        assert get_hashtag() == '#TestHashtag'


def test_process_or_store():
    test_tweet = {
        "id": 123456789,
        "text": "This is a test Tweet",
        "retweet_count": 0
    }
    test_store = []
    process_or_store(test_tweet, test_store)
    target_store = [test_tweet['text']]
    assert test_store == target_store


def test_analysis_decider():
    with unittest.mock.patch('builtins.input', return_value='1'):
        assert analysis_decider() == 1
    with unittest.mock.patch('builtins.input', return_value='2'):
        assert analysis_decider() == 2


def test_rate_error(capfd):
    tweepy_sourcing_error()
    out, err = capfd.readouterr()
    assert out == "Error! Twitter rate limit reach. Wait 15 mins and try again."


def test_tweepy_sourcing_error(capfd):
    tweepy_sourcing_error()
    out, err = capfd.readouterr()
    assert out == "Error! Unable to retrieve tweets."


def test_get_timeline():
    config = ConfigReader('resources/credentials.properties')
    connection = TwitterAuthenticate(config.consumer_key, config.consumer_secret,
                                     config.access_token_key, config.access_token_secret
                                     ).request_auth().make_connection()
    user_id = get_user(connection)
    stored_tweets = get_timeline(connection, user_id)

    assert stored_tweets


def test_search_hashtag():
    assert True is True


def test_data_router():
    assert data_router(1, 'foo') == 'foo'
    assert data_router(2, 'bar') == 'bar'
    assert data_router(3, 'foobar') == ''


def test_load_list():
    target_string_list = ['this', 'is', 'a', 'testfile', 'in', 'newline', 'delimited', 'format']
    assert load_list('resources/test_listfile.txt') == target_string_list
