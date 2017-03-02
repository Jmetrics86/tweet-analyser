# -*- coding: utf-8 -*-

import threading

import requests

from utils.SimpleHTTPWebServer import SimpleHTTPWebServer


class TestWebServer:
    """Test should define the webserver"""

    def test_server(self):
        """Test should start and stop an instance of the SimpleHTTPServer"""

        test_server = SimpleHTTPWebServer('localhost', 8000)
        threading.Thread(target=test_server.start_server).start()

        test_connection = requests.get('http://localhost:8000')

        assassin = threading.Thread(target=test_server.stop_server)
        assassin.daemon = True
        assassin.start()

        assert test_connection.status_code == 200


TestWebServer().test_server()
