# -*- coding: utf-8 -*-

import json
import re
import string
from collections import Counter, defaultdict

import nltk
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


def term_processing(all_terms, stop_words):
    hashtags = []
    uncommon_terms = []

    for term in all_terms:
        if term.startswith('#'):
            hashtags.append(term)
        elif term not in stop_words and not term.startswith(('#', '@')):
            uncommon_terms.append(term)
        else:
            pass

    return hashtags, uncommon_terms


def update_cooccurance(cooccurence_matrix, terms_list):
    for current_term_position in range(len(terms_list) - 1):
        for next_term_position in range(len(terms_list)):
            word1, word2 = sorted([terms_list[current_term_position], terms_list[next_term_position]])
            if word1 != word2:
                cooccurence_matrix[word1][word2] += 1


def document_processing(all_tweets):
    counters = {'all_counter': Counter(),
                'terms_counter': Counter(),
                'hashtag_counter': Counter()}
    term_cooccurence = defaultdict(lambda: defaultdict(int))

    stop_words = common_terms()

    for doc_counter, document in enumerate(all_tweets):
        tweet = json.loads(document)

        all_terms = [term for term in preprocess(tweet['text'])]
        counters['all_counter'].update(all_terms)

        hashtag_list, term_list = term_processing(all_terms, stop_words)
        counters['hashtag_counter'].update(hashtag_list)
        counters['terms_counter'].update(term_list)

        update_cooccurance(term_cooccurence, term_list)

    return counters, term_cooccurence, doc_counter
