# -*- coding: utf-8 -*-

import nltk
import re
import string

from nltk.corpus import stopwords

nltk.download('stopwords')


def regex_tokens():
    """Compile token regex"""

    emoticons_str = r"""(?:[:=;][oO\-]?[D\)\]\(\]/\\OpP])"""

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


def preprocess(string_to_process):
    tokens = tokenize(regex_tokens(), string_to_process)
    tokens = [token.lower() for token in tokens]
    return tokens


def common_terms():
    punctuation = list(string.punctuation)
    stop_words = stopwords.words('english') + punctuation + ['rt', 'via', '…']
    return stop_words
