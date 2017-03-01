# -*- coding: utf-8 -*-

import threading

from utils.WebServer import WebServer


class MultiThreadWebServer(WebServer):

    def start_threaded_server(self):
        threading._start_new_thread(WebServer.start_server(self))

    def stop_threaded_server(self):
        assassin = threading.Thread(target=WebServer.stop_server(self))
        assassin.daemon = True
        assassin.start()
