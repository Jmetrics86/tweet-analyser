from src.data_sourcing import *


def test_process_or_store():
    test_tweet = ''
    test_store = []
    process_or_store(test_tweet, test_store)
    target_store = [test_tweet['text']]
    assert test_store == target_store


def test_load_list():
    target_string_list = ['this', 'is', 'a', 'testfile', 'in', 'newline', 'delimited', 'format']
    assert load_list('resources/test_listfile.txt') == target_string_list


def test_tweepy_sourcing_error():
    assert tweepy_sourcing_error()


def test_data_router():
    assert data_router(1, 'foo') == 'foo'
    assert data_router(2, 'bar') == 'bar'
    assert data_router(3, 'foobar') == ''
