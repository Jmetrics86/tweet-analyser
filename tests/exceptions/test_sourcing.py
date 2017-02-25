# -*- coding: utf-8 -*-

from exceptions.sourcing import rate_error, tweepy_sourcing_error


def test_rate_error(capfd):
    """Test should raise a rate limit exception"""

    rate_error()
    out, err = capfd.readouterr()

    assert out == "Error! Twitter rate limit reach. Wait 15 mins and try again."


def test_tweepy_sourcing_error(capfd):
    """Test should raise a sourcing exception"""

    tweepy_sourcing_error()
    out, err = capfd.readouterr()

    assert out == "Error! Unable to retrieve tweets."
