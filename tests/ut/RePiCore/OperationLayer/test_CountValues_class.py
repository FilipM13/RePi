import pytest
import pandas as pd

from RePiCore.OperationLayer.base import CountValues
from RePiCore.InputLayer.base import TableLike, SingleValues

t = TableLike(pd.DataFrame({
    'col1': [1, 2, 3, 4, 1, 1, 1, 1],
    'col2': [2, 2, 3, 4, 1, 1, 1, 2],
    'col3': ['A', 'B', 'C', 'A', 'B', 'A', 'X', 'X'],
    'col4': [True, True, True, False, False, False, False, False],
}))

s = SingleValues(this=1, that=2, yo_mama='fat')
s.read()

test_cases = {
    'arguments': 'data, column',
    'cases': [
        (t, 'col1'),
        (t, 'col2'),
        (t, 'col3'),
        (t, 'col4'),
    ]
}


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_init(data, column):
    CountValues(
        data=data,
        column=column
    )


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_execute(data, column):
    o = CountValues(
        data=data,
        column=column
    )
    o.execute()
