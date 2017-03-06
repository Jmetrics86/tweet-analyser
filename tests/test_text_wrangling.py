# -*- coding: utf-8 -*-

from data_sourcing import process_or_store
from text_wrangling import *


def test_regex_tokens():
    tokens_re = regex_tokens()
    assert tokens_re


def test_tokenize():
    tokens_re = regex_tokens()

    test_string = "This is a string to TOKENIZE"
    test_hashtag = "#HashTag"
    test_emoji = ":)"
    test_url = "https://www.google.co.uk"
    test_tag = "@test"
    source_string = " ".join([test_string, test_hashtag, test_emoji, test_url, test_tag])

    target = ['This', 'is', 'a', 'string', 'to', 'TOKENIZE',
              '#HashTag', ':)', 'https://www.google.co.uk', '@test']
    assert tokenize(tokens_re, source_string) == target


def test_preprocess():
    test_string = "This IS a DIFFERENT string 2 TOKENIZE"
    test_hashtag = "#HashTag"
    test_emoji = ":)"
    test_url = "https://www.google.co.uk"
    test_tag = "@test"
    source_string = " ".join([test_string, test_hashtag, test_emoji, test_url, test_tag])

    target = ['This', 'is', 'a', 'different', 'string', '2', 'tokenize',
              '#hashtag', ':)', 'https://www.google.co.uk', '@test']

    assert preprocess(source_string) == target


def test_common_terms():
    stopwords = common_terms()
    for test_term in ['rt', 'via', 'a', 'the', 'i', 'to']:
        assert test_term in stopwords


def test_term_processing():
    stopwords = common_terms()
    terms = ['this', 'is', 'a', 'string', '2', 'tokenize',
             '#hashtag', ':)', 'https://www.google.co.uk', '@test']
    target_tags = ['#hashtag']
    target_terms = ['string', '2', 'tokenize', ':)', 'https://www.google.co.uk']
    processed_tags, processed_terms = term_processing(terms, stopwords)
    assert processed_tags == target_tags
    assert processed_terms == target_terms


def test_update_cooccurance():
    """Test should update the co-occurance matrix based on the test terms"""
    term_cooccurence = defaultdict(lambda: defaultdict(int))
    term_list = ['term1', 'term2', 'term1', 'term3']
    update_cooccurance(term_cooccurence, term_list)
    assert term_cooccurence


def test_document_processing():
    """Test should generate terms counters and co-occurance matrix given a collection of tweets"""

    tweet_store = []
    test_tweets = [{"text": "test_one test_two", "foo": "bar"},
                   {"text": "test_one test_two", "foo": "bar"},
                   {"text": "a is of", "foo": "bar"}]

    for tweet in test_tweets:
        process_or_store(tweet, tweet_store)

    target_counts = {
        'all_counter': Counter({'test_one': 2, 'test_two': 2, 'a': 1, 'is': 1, 'of': 1}),
        'hashtag_counter': Counter(),
        'terms_counter': Counter({'test_one': 2, 'test_two': 2})
    }

    counts, term_co, doc_count = document_processing(tweet_store)

    assert counts == target_counts
    assert term_co
    assert doc_count == 2
