# -*- coding: utf-8 -*-

from utils.ListLoader import ListLoader


class TestListLoader:
    def test_load(self):
        """Test should read a newline-delimited file and return a list of strings"""

        target_string_list = ['this', 'is', 'a', 'testfile', 'in', 'newline', 'delimited', 'format']

        test_loader = ListLoader().load('resources/test_listfile.txt')

        assert test_loader == target_string_list
