import pandas as pd
import pytest
import os

from RePiCore.OuputLayer.base import HtmlFile
import RePiCore.CheckingLayer.base as checks
from RePiCore.InputLayer.base import TableLike

table = TableLike(pd.DataFrame(
    {
        'this': ['1', '2', '3', '4', '5', '6'],
        'is': [1, 2, 3, 4, 5, 6],
        'test': ['2023-07-15', '2023-07-16', '2023-07-17', '2023-07-18', '2023-07-19', '2023-07-20'],
        'table': [True, False, True, False, True, False],
    }
))

scatter = TableLike(pd.DataFrame(
    {
        'x data': [0, 0, 9, 9, 6, 6],
        'y data 1': [1, 2, 3, 4, 5, 6],
        'y data 2': [6, 5, 4, 3, 2, 1],
    }
))

histogram = TableLike(pd.DataFrame(
    {
        'serie 1': [
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9,
            9, 9, 9, 9, 9, 9, 9, 9, 9, 8, 7, 8, 7, 8, 8, 7, 8, 7, 8, 7, 8, 7
        ],
        'serie 2': [
            2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4,
            4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7, 8, 9, 7, 8, 9
        ],
        'serie 3': [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9,
            1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4
        ],
    }
))


test_cases = {
    'arguments': 'file_name, report_elements',
    'cases': [
        ('test.html', [
            checks.Plain(text='test test', tag='h1'),
            checks.Plain(text='test test', tag='h2'),
            checks.Plain(text='test test', tag='h3'),
            checks.Plain(text='test test', tag='p'),
            checks.Equals('test equals', 1, 1, 'checks if equals 1'),
            checks.InRange('test in range', 5, 6, 0, 'checks if in <0, 6>'),
            checks.NotInRange('test not in range', 5, 6, 0, 'checks if not in <0, 6>'),
            checks.Table(table),
            # checks.ScatterPlot(scatter, [('x data', 'y data 1')]),
            # checks.ScatterPlot(scatter, [('x data', 'y data 1'), ('x data', 'y data 2')]),
            # checks.ScatterPlot(scatter, [('x data', 'y data 1'), ('x data', 'y data 2')], ['(255,100,0,1)', '(0,255,255,1)']),
            # checks.Histogram(histogram, ['serie 1'], ['(255,0,0,0.3)']),
            # checks.Histogram(histogram, ['serie 1', 'serie 2'], ['(255,0,0,0.3)', '(0,255,0,0.3)']),
            # checks.Histogram(histogram, ['serie 1', 'serie 2', 'serie 3'], ['(255,0,0,0.3)', '(0,255,0,0.3)', '(0,0,255,0.3)']),
            # checks.Histogram(histogram, ['serie 1']),
            # checks.Histogram(histogram, ['serie 1', 'serie 2', 'serie 3']),
        ])
    ]
}


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_init(file_name, report_elements):
    HtmlFile(file_name, report_elements)


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_generate(file_name, report_elements):
    o = HtmlFile(file_name, report_elements)
    o.generate()
    os.remove(file_name)
