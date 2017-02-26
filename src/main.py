# -*- coding: utf-8 -*-

import term_analysis as ta
from data_sourcing import analysis_decider, data_router
from text_wrangling import document_processing
from utils.ConfigReader import ConfigReader
from utils.TwitterAuthenticate import TwitterAuthenticate

if __name__ == '__main__':
    config = ConfigReader('resources/credentials.properties')

    twitter_connection = TwitterAuthenticate(config.consumer_key, config.consumer_secret,
                                             config.access_token_key, config.access_token_secret
                                             ).request_auth().make_connection()

    source_choice = analysis_decider()
    all_tweets = data_router(source_choice, twitter_connection)

    word_counters, co_occ_matrix, total_docs = document_processing(all_tweets)

    top_pairs = ta.top_cooccorrent_terms(co_occ_matrix)

    most_common_terms = word_counters['terms_counter'].most_common(20)
    # generate_report(most_common_terms)

    prob_term_matrix, prob_terms = ta.term_probabilities(total_docs, word_counters['all_counter'], co_occ_matrix)

    pmi = ta.calculate_pmi(prob_terms, co_occ_matrix, prob_term_matrix)
    semantic_orientation = ta.semantic_orientation(prob_terms, pmi)
    top_positive_terms, top_negative_terms = ta.top_semantic_terms(semantic_orientation, 10)
