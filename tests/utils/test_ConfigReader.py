# -*- coding: utf-8 -*-

from utils.ConfigReader import ConfigReader


def test_config_reader():
    """Test should read config properties from the properties file"""
    test_config = ConfigReader('resources/credentials.properties')
    assert test_config.consumer_key
    assert test_config.consumer_secret
    assert test_config.access_token_key
    assert test_config.access_token_secret
