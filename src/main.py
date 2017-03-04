# -*- coding: utf-8 -*-

import term_analysis as ta
from data_sourcing import analysis_decider, data_router
from report.ReportManager import ReportManager
from report.data_visualisation import bar_chart, timeseries_chart, key_value_table
from text_wrangling import document_processing
from utils.ConfigReader import ConfigReader
from utils.TwitterAuthenticate import TwitterAuthenticate

if __name__ == '__main__':
    # Authenticate and open the connection to Twitter
    config = ConfigReader('resources/credentials.properties')
    twitter_connection = TwitterAuthenticate(config.consumer_key, config.consumer_secret,
                                             config.access_token_key, config.access_token_secret
                                             ).request_auth().make_connection()

    # Ask user which data source to get and retrieve all tweets
    source_choice = analysis_decider()
    all_tweets = data_router(source_choice, twitter_connection)

    # Process all tweets into counters and co-occurance matrix
    word_counters, tweet_dates, co_occ_matrix = document_processing(all_tweets)

    # Calculate probability matrix of each term appearing
    prob_term_matrix, prob_terms = ta.term_probabilities(
        word_counters['doc_counter'],
        word_counters['all_counter'],
        co_occ_matrix)

    # Calculate Semantic Orientation of term and return best/worst terms
    pmi = ta.calculate_pmi(prob_terms, co_occ_matrix, prob_term_matrix)
    semantic_orientation = ta.semantic_orientation(prob_terms, pmi)
    top_positive_terms, top_negative_terms = ta.top_semantic_terms(semantic_orientation, 10)

    print(top_positive_terms)
    print(top_negative_terms)

    # Generate vincent graphs for aggregated data
    key_value_table(top_positive_terms + top_negative_terms)
    timeseries_chart(ta.tweet_timeseries(tweet_dates))
    bar_chart('top_terms', word_counters['terms_counter'].most_common(10))
    bar_chart('top_pairs', ta.top_cooccorrent_terms(co_occ_matrix)[:10])
    bar_chart('top_hashtags', word_counters['hashtag_counter'].most_common(10))
    bar_chart('top_usertags', word_counters['tag_counter'].most_common(10))

    # Run report on local webserver
    ReportManager('user').run_report(2, 'localhost', 8000)
