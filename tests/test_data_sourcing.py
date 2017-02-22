# -*- coding: utf-8 -*-

import unittest.mock
from configparser import RawConfigParser

from data_sourcing import *
from twitter_authenticate import Authorise


def test_get_user():
    api_keys = RawConfigParser()
    api_keys.read('resources/credentials.properties')
    c_key = api_keys.get('apiKeys', 'consumer.key')
    c_secret = api_keys.get('apiKeys', 'consumer.secret')
    t_key = api_keys.get('apiKeys', 'accessToken.key')
    t_secret = api_keys.get('apiKeys', 'accessToken.secret')

    twitter_connection = Authorise(c_key, c_secret, t_key, t_secret).request_auth().make_connection()

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
    assert True is True


def test_rate_error(capfd):
    tweepy_sourcing_error()
    out, err = capfd.readouterr()
    assert out == "Error! Twitter rate limit reach. Wait 15 mins and try again."


def test_tweepy_sourcing_error(capfd):
    tweepy_sourcing_error()
    out, err = capfd.readouterr()
    assert out == "Error! Unable to retrieve tweets."


def test_get_timeline():
    assert True is True


def test_search_hashtag():
    assert True is True


def test_data_router():
    assert data_router(1, 'foo') == 'foo'
    assert data_router(2, 'bar') == 'bar'
    assert data_router(3, 'foobar') == ''


def test_load_list():
    target_string_list = ['this', 'is', 'a', 'testfile', 'in', 'newline', 'delimited', 'format']
    assert load_list('resources/test_listfile.txt') == target_string_list
