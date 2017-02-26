# -*- coding: utf-8 -*-

import time

from report.data_visualisation import bar_chart
from report.web_server import WebServer


def generate_report(dataset):
    """Generates Twitter Report and publishes to WebServer"""

    WebServer().run_server()
    bar_chart(dataset)
    sleep_delay_mins = 5

    print("Report ready to view at http://localhost:8888/report/chart.html \n"
          "Report will be available for the next %s minutes" % sleep_delay_mins)
    time.sleep(sleep_delay_mins * 60)
