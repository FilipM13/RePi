import pytest
import pandas as pd

from RePiCore.CheckingLayer.base import Histogram
from RePiCore.InputLayer.base import TableLike

t = TableLike(pd.DataFrame({
    'col1': [1, 2, 3, 4, 1, 1, 1, 1],
    'col2': [2, 2, 3, 4, 1, 1, 1, 2]
}))

test_cases = {
    'arguments': 'data, series, colors',
    'cases': [
        (t, ['col1'], ['(255,0,0,1)']),
        (t, ['col1', 'col2'], ['(255,0,0,1)', '(255,0,255,1)']),
        (t, ['col1', 'col2'], None),
        (t, [], None),
    ]
}


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_init(data, series, colors):
    Histogram(data, series, colors)


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_create_element(data, series, colors):
    o = Histogram(data, series, colors)
    o.create_element()
