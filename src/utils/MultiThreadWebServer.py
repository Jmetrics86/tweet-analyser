# -*- coding: utf-8 -*-

import threading

from utils.SimpleHTTPWebServer import SimpleHTTPWebServer


class MultiThreadWebServer(SimpleHTTPWebServer):

    def __init__(self, hostname, port):
        super().__init__(hostname, port)

    def start_threaded_server(self):
        threading.Thread(target=MultiThreadWebServer.start_server).start()

    def stop_threaded_server(self):
        assassin = threading.Thread(target=MultiThreadWebServer.stop_server)
        assassin.daemon = True
        assassin.start()
