# -*- coding: utf-8 -*-

import threading

import utils.WebServer


class MultiThreadWebServer(utils.WebServer):
    def __init__(self):
        self = utils.WebServer.WebServer.__init__()

    def start_threaded_server(self):
        threading._start_new_thread(utils.WebServer.WebServer.start_server())

    def stop_threaded_server(self):
        assassin = threading.Thread(target=utils.WebServer.WebServer.stop_server())
        assassin.daemon = True
        assassin.start()
