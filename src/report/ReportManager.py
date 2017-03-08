# -*- coding: utf-8 -*-

import threading
import time

from utils.SimpleHTTPWebServer import SimpleHTTPWebServer
from utils.WebsiteToPdf import WebSiteToPdf


class ReportManager:
    """Generates Twitter Report and publishes to WebServer"""

    def __init__(self, url, port):
        self.url = str(url)
        self.port = int(port)
        self.address = 'http://' + url + ":" + str(port) + "/report/tweet_analysis.html"

    def run_report(self, minutes_to_wait):
        server = SimpleHTTPWebServer(self.url, self.port)
        threading.Thread(target=server.start_server).start()

        print("Report ready to view at %s \n"
              "Report will be available for the next %s minutes" % (self.address, minutes_to_wait))
        time.sleep(minutes_to_wait * 60)

        WebSiteToPdf(self.address, "tweet_analysis_report_" + time.strftime("%Y%m%d%H%M%S") + ".pdf").convert_site()

        assassin = threading.Thread(target=server.stop_server)
        assassin.daemon = True
        assassin.start()
