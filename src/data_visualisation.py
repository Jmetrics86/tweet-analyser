# -*- coding: utf-8 -*-

import vincent


def bar_chart(key_freq):
    labels, freq = zip(*key_freq)
    data = {'data': freq, 'x': labels}

    bar = vincent.Bar(data, iter_idx='x')
    bar.display()


def timeseries_chart(pandas_timeseries):
    time_chart = vincent.Line(pandas_timeseries)
    time_chart.axis_titles(x='Time', y='Freq')
    time_chart.display()
