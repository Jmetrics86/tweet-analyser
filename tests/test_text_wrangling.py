# -*- coding: utf-8 -*-

from text_wrangling import *


def test_regex_tokens():
    assert True is True


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
    assert True is True
