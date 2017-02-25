# -*- coding: utf-8 -*-


def rate_error():
    """Throws Twitter rate limit error"""
    print("Error! Twitter rate limit reach. Wait 15 mins and try again.")


def tweepy_sourcing_error():
    """Throws general sourcing error"""
    print("Error! Unable to retrieve tweets.")
