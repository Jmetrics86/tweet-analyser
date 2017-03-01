# -*- coding: utf-8 -*-

import threading

import report.WebServer


class MultiThreadWebServer(report.WebServer):
    def __init__(self):
        self = report.WebServer.WebServer.__init__()

    def start_threaded_server(self):
        threading._start_new_thread(report.WebServer.WebServer.start_server())

    def stop_threaded_server(self):
        assassin = threading.Thread(target=report.WebServer.WebServer.stop_server())
        assassin.daemon = True
        assassin.start()
