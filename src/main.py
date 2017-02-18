# -*- coding: utf-8 -*-

from src.authenticate import Authorise
from src.data_sourcing import get_user, analysis_decider

if __name__ == '__main__':
    api_connection = Authorise
    consumer_key = input('Enter consumer key: ')
    consumer_secret = input('Enter consumer secret: ')
    twitter_connection = api_connection(consumer_key, consumer_secret).request_token().make_connection()

    source_choice = analysis_decider()