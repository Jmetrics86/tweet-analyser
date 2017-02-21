from src.data_sourcing import *


def test_process_or_store():
    test_tweet = ''
    test_store = []
    process_or_store(test_tweet, test_store)
    target_store = [test_tweet['text']]
    assert test_store == target_store
