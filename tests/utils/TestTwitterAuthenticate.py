# -*- coding: utf-8 -*-

from utils.ConfigReader import ConfigReader
from utils.TwitterAuthenticate import TwitterAuthenticate


class TestTwitterAuthenticate:
    def test_twitter_authenticate(self):
        """Test should pass config properties from the properties file"""

        config = ConfigReader('resources/credentials.properties')
        authoriser = TwitterAuthenticate(config.consumer_key, config.consumer_secret,
                                         config.access_token_key, config.access_token_secret)

        assert authoriser.consumer_key
        assert authoriser.consumer_secret
        assert authoriser.token_key
        assert authoriser.token_secret
        assert authoriser.auth == ''

    def test_request_auth(self):
        config = ConfigReader('resources/credentials.properties')

        authoriser = TwitterAuthenticate(
            config.consumer_key, config.consumer_secret,
            config.access_token_key, config.access_token_secret
        ).request_auth()

        assert authoriser.auth

    def test_make_connection(self):
        config = ConfigReader('resources/credentials.properties')
        connection = TwitterAuthenticate(config.consumer_key, config.consumer_secret,
                                         config.access_token_key, config.access_token_secret
                                         ).request_auth().make_connection()

        assert connection
