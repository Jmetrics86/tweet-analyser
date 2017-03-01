# -*- coding: utf-8 -*-

import http.server
import socketserver


class WebServer(object):
    def __init__(self):
        self.port = 8000
        self.handler = http.server.SimpleHTTPRequestHandler
        self.httpd = socketserver.TCPServer(("", self.port), self.handler)

    def start_server(self):
        self.httpd.serve_forever()

    def stop_server(self):
        self.httpd.shutdown()
