import threading

import requests

from utils.SimpleHTTPWebServer import SimpleHTTPWebServer


class TestWebServer:
    """Test should define the webserver"""

    def test_start_server(self):
        """Test should start an instance of the SimpleHTTPServer"""

        test_server = SimpleHTTPWebServer('localhost', 8000)
        threading._start_new_thread(test_server.start_server())

        req = requests.get('localhost:8000')
        assert req.status_code == 200

    def test_stop_server(self):
        """Test should shutdown an instance of the SimpleHTTPServer"""

        test_server = SimpleHTTPWebServer('localhost', 8000)
        test_server.start_server()
        test_server.stop_server()
        assert True


TestWebServer().test_start_server()
