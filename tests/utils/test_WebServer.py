import http.server
import socketserver

from utils.WebServer import WebServer


def test_web_server():
    """Test should define the webserver"""

    test_server = WebServer()

    assert test_server.port == 8000
    assert test_server.handler == http.server.SimpleHTTPRequestHandler
    assert test_server.httpd == socketserver.TCPServer(("", 8000), http.server.SimpleHTTPRequestHandler)


def test_start_server():
    """Test should start an instance of the SimpleHTTPServer"""

    test_server = WebServer()
    test_server.start_server()
    assert True


def test_stop_server():
    """Test should shutdown an instance of the SimpleHTTPServer"""

    test_server = WebServer()
    test_server.start_server()
    test_server.stop_server()
    assert True


test_start_server()
