# -*- coding: utf-8 -*-

from src.utils.ConfigReader import ConfigReader


class TestConfigReader:
    """Test should read config properties from the properties file"""

    def test_config_reader(self):
        test_config = ConfigReader('resources/credentials.properties')
        assert test_config.consumer_key
        assert test_config.consumer_secret
        assert test_config.access_token_key
        assert test_config.access_token_secret
