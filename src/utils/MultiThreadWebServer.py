# -*- coding: utf-8 -*-

import threading

from utils.SimpleHTTPWebServer import SimpleHTTPWebServer


class MultiThreadWebServer(SimpleHTTPWebServer):
    def __init__(self, hostname, port):
        super().__init__(hostname, port)

    def start_threaded_server(self):
        threading._start_new_thread(MultiThreadWebServer.start_server(self))

    def stop_threaded_server(self):
        assassin = threading.Thread(target=MultiThreadWebServer.stop_server(self))
        assassin.daemon = True
        assassin.start()
