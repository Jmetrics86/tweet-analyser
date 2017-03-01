# -*- coding: utf-8 -*-

import time

from report.WebServer import WebServer


class ReportManager:
    """Generates Twitter Report and publishes to WebServer"""

    def __init__(self, style):
        self.report_style = style

    def prepare_report(self):
        WebServer().run_server()

    def run_report(self, minutes_to_wait):
        self.prepare_report()
        print("Report ready to view at http://localhost:8888/report/chart.html \n"
              "Report will be available for the next %s minutes" % minutes_to_wait)
        time.sleep(minutes_to_wait * 60)
