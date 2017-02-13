# -*- coding: utf-8 -*-

import re


def emoticons():
    """Defines regex string for emoticons"""
    return r"""(?:[:=;][oO\-]?[D\)\]\(\]/\\OpP])"""


def regex_emoticons(emoticons_str):
    """Compile emoticon regex"""
    return re.compile(r'^' + emoticons_str + '$', re.VERBOSE | re.IGNORECASE)


def regex_tokens(emoticons_str):
    """Compile token regex"""

    regex_str = [
        emoticons_str,
        r'<[^>]+>',  # HTML tags
        r'(?:@[\w_]+)',  # @-mentions
        r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",  # hash-tags
        r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',  # URLs
        r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # numbers
        r"(?:[a-z][a-z'\-_]+[a-z])",  # words with - and '
        r'(?:[\w_]+)',  # other words
        r'(?:\S)'  # anything else
    ]

    return re.compile(r'(' + '|'.join(regex_str) + ')', re.VERBOSE | re.IGNORECASE)


def tokenize(tokens_re, string_to_tokenize):
    """Tokenizes a string to a list of strings"""
    return tokens_re.findall(string_to_tokenize)


def preprocess(string_to_process, lowercase=False):
    tokens = tokenize(regex_emoticons())