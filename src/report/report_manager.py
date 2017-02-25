# -*- coding: utf-8 -*-

from report.data_visualisation import bar_chart
from report.web_server import WebServer


def generate_report(key_frequency):
    WebServer().run_server()
    bar_chart(key_frequency)
