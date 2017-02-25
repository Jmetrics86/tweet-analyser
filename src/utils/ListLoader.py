# -*- coding: utf-8 -*-


class ListLoader:
    """Loads \n-delimited files and returns lists of strings"""

    def __init__(self):
        self.string_list = []

    def load(self, list_file):
        with open(list_file, 'r') as file:
            self.string_list = file.read().splitlines()
        file.close()

        return self.string_list
