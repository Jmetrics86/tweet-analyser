# -*- coding: utf-8 -*-

from configparser import RawConfigParser

from src.data_visualisation import bar_chart
from src.term_analysis import top_cooccorrent_terms, term_probabilities
from src.text_wrangling import document_processing
from src.twitter_authenticate import Authorise
from src.twitter_sourcing import analysis_decider, data_router

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

    word_counters, co_occ_matrix, total_docs = document_processing(all_tweets)

    top_pairs = top_cooccorrent_terms(co_occ_matrix)

    most_common_terms = word_counters['terms_counter'].most_common(20)
    bar_chart(most_common_terms)

    probability_of_terms = term_probabilities(total_docs, word_counters['all_counters'], co_occ_matrix)
