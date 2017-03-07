# -*- coding: utf-8 -*-

import threading
import time

from utils.SimpleHTTPWebServer import SimpleHTTPWebServer


class ReportManager:
    """Generates Twitter Report and publishes to WebServer"""

    def __init__(self, style):
        self.report_style = style

    def run_report(self, minutes_to_wait, url, port):
        server = SimpleHTTPWebServer(url, port)
        threading.Thread(target=server.start_server).start()

        print("Report ready to view at http://%s:%d/report/tweet_analysis.html \n"
              "Report will be available for the next %s minutes" % (url, port, minutes_to_wait))
        time.sleep(minutes_to_wait * 60)

        assassin = threading.Thread(target=server.stop_server)
        assassin.daemon = True
        assassin.start()
