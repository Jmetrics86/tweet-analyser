# -*- coding: utf-8 -*-

import json

import vincent


def bar_chart(source, key_freq):
    """Generates JSON document for bar chart visualisation using vincent"""

    labels, freq = zip(*key_freq)
    data = {'data': freq, 'x': labels}

    bar = vincent.Bar(data, iter_idx='x')
    bar.to_json('report/%s_freq.json' % source)


def timeseries_chart(pandas_timeseries):
    """Generates JSON document for line chart visualisation using vincent"""

    time_chart = vincent.Line(pandas_timeseries)
    time_chart.axis_titles(x='Time', y='Freq')

    time_chart.to_json('report/time_series.json')


def key_value_table(tuple_list):
    """Generates JSON document for table visualisation"""

    with open('report/semantic_terms.json', 'w') as semantic_json:
        json.dump(dict(tuple_list), semantic_json)
