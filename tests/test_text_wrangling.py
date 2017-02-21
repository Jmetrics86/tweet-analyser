# -*- coding: utf-8 -*-

from src.text_wrangling import *


def test_tokenize():
    test_string = "this is a string to tokenize"
    test_hashtag = "#hashtag"
    test_emoji = ":)"
    test_url = "https://www.google.co.uk"
    test_tag = "@test"
    source_string = " ".join([test_string, test_hashtag, test_emoji, test_url, test_tag])

    target = ['this', 'is', 'a', 'string', 'to', 'tokenize',
              '#hashtag', ':)', 'https://www.google.co.uk', '@test']
    assert tokenize('', source_string) == target
