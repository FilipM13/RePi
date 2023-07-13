import pytest
import pandas as pd

from RePiCore.CheckingLayer.base import Table
from RePiCore.InputLayer.base import TableLike

t = TableLike(pd.DataFrame({
    'col1': [1, 2, 3, 4, 1, 1, 1, 1],
    'col2': [2, 2, 3, 4, 1, 1, 1, 2]
}))

test_cases = {
    'arguments': 'data, index',
    'cases': [
        (t, True),
        (t, False),
    ]
}


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_init(data, index):
    Table(data, index)


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_to_html(data, index):
    o = Table(data, index)
    o.to_html()
