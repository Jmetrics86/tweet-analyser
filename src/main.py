# -*- coding: utf-8 -*-

import json
from collections import Counter
from configparser import RawConfigParser

from src.authenticate import Authorise
from src.data_sourcing import analysis_decider, data_router
from src.data_wrangling import preprocess, common_terms

if __name__ == '__main__':
    api_connection = Authorise

    api_keys = RawConfigParser()
    api_keys.read('resources/credentials.properties')
    c_key = api_keys.get('apiKeys', 'consumer.key')
    c_secret = api_keys.get('apiKeys', 'consumer.secret')
    t_key = api_keys.get('apiKeys', 'accessToken.key')
    t_secret = api_keys.get('apiKeys', 'accessToken.secret')

    twitter_connection = api_connection(c_key, c_secret, t_key, t_secret).request_auth().make_connection()

    source_choice = analysis_decider()
    all_tweets = data_router(source_choice, twitter_connection)

    all_counter = Counter()
    terms_counter = Counter()
    stop_words = common_terms()

    for doc_counter, document in enumerate(all_tweets):
        tweet = json.loads(document)
        all_terms = [term for term in preprocess(tweet['text'])]
        hashtags = []
        uncommon_terms = []

        for term in all_terms:
            if term.startswith('#'):
                hashtags.append(term)
            elif term not in stop_words and not term.startswith(('#', '@')):
                uncommon_terms.append(term)
            else:
                pass

        all_counter.update(all_terms)
        terms_counter.update(uncommon_terms)
