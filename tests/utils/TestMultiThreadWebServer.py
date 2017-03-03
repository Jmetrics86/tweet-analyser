# -*- coding: utf-8 -*-

import requests

from utils.MultiThreadWebServer import MultiThreadWebServer


class TestMultiThreadedWebServer:
    """Test class should start up and shutdown the webserver using multithreading"""

    def test_threaded_server(self):
        test_server = MultiThreadWebServer('localhost', 9000)
        test_server.start_threaded_server()

        test_connection = requests.get('http://localhost:9000')

        test_server.stop_threaded_server()

        assert test_connection.status_code == 200
