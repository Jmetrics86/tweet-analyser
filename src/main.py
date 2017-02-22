# -*- coding: utf-8 -*-

from configparser import RawConfigParser

import term_analysis
from data_sourcing import analysis_decider, data_router
from data_visualisation import bar_chart
from text_wrangling import document_processing
from twitter_authenticate import Authorise

if __name__ == '__main__':

    api_keys = RawConfigParser()
    api_keys.read('resources/credentials.properties')
    c_key = api_keys.get('apiKeys', 'consumer.key')
    c_secret = api_keys.get('apiKeys', 'consumer.secret')
    t_key = api_keys.get('apiKeys', 'accessToken.key')
    t_secret = api_keys.get('apiKeys', 'accessToken.secret')

    twitter_connection = Authorise(c_key, c_secret, t_key, t_secret).request_auth().make_connection()

    source_choice = analysis_decider()
    all_tweets = data_router(source_choice, twitter_connection)

    word_counters, co_occ_matrix, total_docs = document_processing(all_tweets)

    top_pairs = term_analysis.top_cooccorrent_terms(co_occ_matrix)

    most_common_terms = word_counters['terms_counter'].most_common(20)
    bar_chart(most_common_terms)

    probability_term_matrix, probability_of_terms = term_analysis.term_probabilities(total_docs,
                                                                                     word_counters['all_counters'],
                                                                                     co_occ_matrix)
    pointwise_MI = term_analysis.calculate_pmi(probability_of_terms, co_occ_matrix, probability_term_matrix)
    semantic_orientation = term_analysis.calculate_semantic_orientation(probability_of_terms, pointwise_MI)
    top_positive_terms, top_negative_terms = term_analysis.top_semantic_terms(semantic_orientation, 10)
