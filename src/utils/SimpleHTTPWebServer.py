# -*- coding: utf-8 -*-

import http.server
import socketserver


class SimpleHTTPWebServer(object):
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port
        self.handler = http.server.SimpleHTTPRequestHandler
        self.httpd = socketserver.TCPServer((self.hostname, self.port), self.handler)

    def start_server(self):
        self.httpd.serve_forever()

    def stop_server(self):
        self.httpd.shutdown()
