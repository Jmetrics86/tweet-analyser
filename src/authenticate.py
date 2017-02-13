# -*- coding: utf-8 -*-

from tweepy import OAuthHandler, TweepError, API

class Authorise:
    """Class to handle the authorisation and connection to Twitter"""

    def __init__(self, consumer_key, consumer_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.redirect_url = ''
        self.callback_url = ''
        self.request_key = ''
        self.request_secret = ''
        self.auth = ''

    def request_token(self):
        self.auth = OAuthHandler(self.consumer_key, self.consumer_secret, self.callback_url)
        try:
            self.redirect_url = self.auth.get_authorization_url()
        except TweepError:
            print("Error! Failed to get request token.")
        self.request_key = self.auth.request_token['oauth_token']
        self.request_secret = self.auth.request_token['oauth_token_secret']
        return self

    def make_connection(self):
        try:
            self.auth.set_access_token(self.request_key, self.request_secret)
            api = API(self.auth)
        except:
            print("Error! Failed to authorise api connection.")
        return api


if __name__ == '__main__':
    consumer_key = input('Enter consumer key: ')
    consumer_secret = input('Enter consumer secret: ')

    twitter_connection = Authorise(consumer_key, consumer_secret).request_token().make_connection()
