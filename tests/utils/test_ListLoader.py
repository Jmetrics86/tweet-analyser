# -*- coding: utf-8 -*-

from utils.ListLoader import ListLoader


def test_load_list():
    """Test should read a newline-delimited file and return a list of strings"""

    target_string_list = ['this', 'is', 'a', 'testfile', 'in', 'newline', 'delimited', 'format']

    assert ListLoader().load('resources/test_listfile.txt') == target_string_list


test_load_list()
