# -*- coding: utf-8 -*-

import vincent


def bar_chart(key_freq):
    """Generates JSON document for bar chart visualisation using vincent"""

    labels, freq = zip(*key_freq)
    data = {'data': freq, 'x': labels}

    bar = vincent.Bar(data, iter_idx='x')
    bar.to_json('report/term_freq.json')


def timeseries_chart(pandas_timeseries):
    """Generates JSON document for line chart visualisation using vincent"""

    time_chart = vincent.Line(pandas_timeseries)
    time_chart.axis_titles(x='Time', y='Freq')

    time_chart.to_json('report/time_series.json')
