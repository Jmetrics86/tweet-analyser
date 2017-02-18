# -*- coding: utf-8 -*-

from tweepy import OAuthHandler, TweepError, API

class Authorise:
    """Class to handle the authorisation and connection to Twitter"""

    def __init__(self, consumer_key, consumer_secret, token_key, token_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.token_key = token_key
        self.token_secret = token_secret
        self.auth = ''

    def request_auth(self):
        try:
            self.auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        except TweepError:
            print("Error! Failed to get request token.")
        return self

    def make_connection(self):
        api = ''
        try:
            self.auth.set_access_token(self.token_key, self.token_secret)
            api = API(self.auth)
        except:
            print("Error! Failed to authorise api connection.")
        return api


if __name__ == '__main__':
    c_key = input('Enter consumer key: ')
    c_secret = input('Enter consumer secret: ')
    t_key = input('Enter access-token key: ')
    t_secret = input('Enter access-token secret: ')

    twitter_connection = Authorise(c_key, c_secret, t_key, t_secret).request_auth().make_connection()
