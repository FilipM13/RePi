import pytest
import pandas as pd

from RePiCore.OperationLayer.base import ColumnCompareMatrix
from RePiCore.InputLayer.base import TableLike, SingleValues

t = TableLike(pd.DataFrame({
    'c1': ['B', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A'],
    'c2': ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
    'c3': ['C', 'C', 'C', 'A', 'A', 'C', 'C', 'C', 'A', 'A', ],
}))
s = SingleValues(this=1, that=2, yo_mama='fat')
s.read()

test_cases = {
    'arguments': 'data, column1, column2',
    'cases': [
        (t, 'c1', 'c2'),
        (t, 'c1', 'c3'),
    ]
}


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_init(data, column1, column2):
    ColumnCompareMatrix(
        data=data,
        column1=column1,
        column2=column2
    )


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_execute(data, column1, column2):
    o = ColumnCompareMatrix(
        data=data,
        column1=column1,
        column2=column2
    )
    o.execute()
