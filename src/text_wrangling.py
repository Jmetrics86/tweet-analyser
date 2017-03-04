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
    """Pre-processes strings into standardised lowercase tokens"""

    tokens = tokenize(regex_tokens(), string_to_process)
    tokens = [token.lower() for token in tokens]

    return tokens


def common_terms():
    """Generates list of common english stop words and punctuation"""

    punctuation = list(string.punctuation)
    stop_words = stopwords.words('english') + punctuation + ['rt', 'via', '…']

    return stop_words


def term_processing(all_terms, stop_words):
    """Processes all terms in a tweet into lists of hashtags, usertags and uncommon terms"""

    hashtags = []
    usertags = []
    uncommon_terms = []

    for term in all_terms:

        if term.startswith('#'):
            hashtags.append(term)

        elif term.startswith('@'):
            usertags.append(term)

        elif term not in stop_words and not term.startswith(('#', '@')):
            uncommon_terms.append(term)

        else:
            pass

    return hashtags, usertags, uncommon_terms


def update_cooccurance(cooccurence_matrix, terms_list):
    """Iterates through single tweet and updates co-occurance matrix for words appearing in same message"""

    for term_position1 in range(len(terms_list) - 1):

        for term_position2 in range(len(terms_list)):

            word1, word2 = sorted([terms_list[term_position1], terms_list[term_position2]])

            if word1 != word2:
                cooccurence_matrix[word1][word2] += 1


def document_processing(all_tweets):
    """
    Main processing function.
    Iterates all docs/tweets and returns counters of terms, and term co-occurance matrix
    """

    counters = {'all_counter': Counter(),
                'terms_counter': Counter(),
                'hashtag_counter': Counter(),
                'tag_counter': Counter()}
    term_cooccurence = defaultdict(lambda: defaultdict(int))
    dates = []

    stop_words = common_terms()

    for doc_counter, document in enumerate(all_tweets):
        tweet = json.loads(document)

        all_terms = [term for term in preprocess(tweet['text'])]
        counters['all_counter'].update(all_terms)

        hashtag_list, tag_list, term_list = term_processing(all_terms, stop_words)
        counters['hashtag_counter'].update(hashtag_list)
        counters['tag_counter'].update(tag_list)
        counters['terms_counter'].update(term_list)

        dates.append(tweet['created_at'])

        update_cooccurance(term_cooccurence, term_list)

    try:
        counters['doc_counter'] = doc_counter

    except ValueError:
        counters['doc_counter'] = 0

    return counters, dates, term_cooccurence
