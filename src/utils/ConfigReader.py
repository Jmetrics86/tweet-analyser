# -*- coding: utf-8 -*-

from configparser import RawConfigParser


class ConfigReader:
    def __init__(self, credentials_file):
        api_keys = RawConfigParser()
        api_keys.read(credentials_file)
        self.consumer_key = api_keys.get('apiKeys', 'consumer.key')
        self.consumer_secret = api_keys.get('apiKeys', 'consumer.secret')
        self.access_token_key = api_keys.get('apiKeys', 'accessToken.key')
        self.access_token_secret = api_keys.get('apiKeys', 'accessToken.secret')
