# -*- coding: utf-8 -*-

import unittest.mock

from src.data_sourcing import *
from src.utils.ConfigReader import ConfigReader
from src.utils.TwitterAuthenticate import TwitterAuthenticate


def test_get_user():
    """Test should take input username and return specified userId"""

    config = ConfigReader('resources/credentials.properties')

    twitter_connection = TwitterAuthenticate(config.consumer_key, config.consumer_secret,
                                             config.access_token_key, config.access_token_secret
                                             ).request_auth().make_connection()

    with unittest.mock.patch('builtins.input', return_value='HomerSimpson'):
        assert get_user(twitter_connection) == 758608


def test_get_hashtag():
    """Test should tale input hashtag and return standardised hashtag"""

    with unittest.mock.patch('builtins.input', return_value='#TestHashtag'):
        assert get_hashtag() == '#TestHashtag'

    with unittest.mock.patch('builtins.input', return_value='TestHashtag'):
        assert get_hashtag() == '#TestHashtag'


def test_process_or_store():
    """Test should process test tweet to json document and update a list"""

    test_tweet = {
        "id": 123456789,
        "text": "This is a test Tweet",
        "retweet_count": 0}
    test_store = []
    target_store = [test_tweet]

    process_or_store(test_tweet, test_store)

    assert json.loads(test_store[0]) == target_store[0]


def test_analysis_decider():
    """Test should take a string of 1 or 2 and return the int"""

    with unittest.mock.patch('builtins.input', return_value='1'):
        assert analysis_decider() == 1

    with unittest.mock.patch('builtins.input', return_value='2'):
        assert analysis_decider() == 2


def test_get_timeline():
    """Test should return stored tweets from a specified user timeline"""

    config = ConfigReader('resources/credentials.properties')
    connection = TwitterAuthenticate(config.consumer_key, config.consumer_secret,
                                     config.access_token_key, config.access_token_secret
                                     ).request_auth().make_connection()

    user_id = 758608
    stored_tweets = get_timeline(connection, user_id)

    assert stored_tweets


def test_search_hashtag():
    """Test should return stored tweets from a specified hashtag search"""

    config = ConfigReader('resources/credentials.properties')
    connection = TwitterAuthenticate(config.consumer_key, config.consumer_secret,
                                     config.access_token_key, config.access_token_secret
                                     ).request_auth().make_connection()

    hashtag = '#TestTag'
    stored_tweets = search_hashtag(connection, hashtag)

    assert stored_tweets


def test_data_router():
    """Test should return the relevant tweets based on the specified user analysis"""

    config = ConfigReader('resources/credentials.properties')
    connection = TwitterAuthenticate(config.consumer_key, config.consumer_secret,
                                     config.access_token_key, config.access_token_secret
                                     ).request_auth().make_connection()

    with unittest.mock.patch('builtins.input', return_value='HomerSimpson'):
        assert data_router(1, connection)

    with unittest.mock.patch('builtins.input', return_value='#hashtag'):
        assert data_router(2, connection)

    assert not data_router(3, connection)
