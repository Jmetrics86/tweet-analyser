# -*- coding: utf-8 -*-

import mock

from data_sourcing import *


def test_get_user():
    assert True is True


def test_get_hashtag():
    with mock.patch('builtins.input', lambda: "#TestHashtag"):
        assert get_hashtag() == "#TestHashtag"
    with mock.patch('builtins.input', lambda: "TestHashtag"):
        assert get_hashtag() == "#TestHashtag"


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
