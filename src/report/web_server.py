# -*- coding: utf-8 -*-

import subprocess


class WebServer:
    def __init__(self):
        self.start_server = 'python -m http.server 8888 &'

    def run_server(self):
        subprocess.call(self.start_server)
