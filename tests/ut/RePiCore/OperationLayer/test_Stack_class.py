import pytest
import pandas as pd

from RePiCore.OperationLayer.base import Stack
from RePiCore.InputLayer.base import TableLike, SingleValues

t1 = TableLike(pd.DataFrame({
    'col1': [1, 2, 3, 4, 1, 1, 1, 1],
    'col2': [2, 2, 3, 4, 1, 1, 1, 2]
}))

t2 = TableLike(pd.DataFrame({
    'col3': [1, 2, 3, 4, 1, 1, 1, 1],
    'col4': [2, 2, 3, 4, 1, 1, 1, 2]
}))

t3 = TableLike(pd.DataFrame({
    'col1': [1, 2, 3, 4, 1, 1, 1, 1],
    'col5': [2, 2, 3, 4, 1, 1, 1, 2]
}))

s = SingleValues(this=1, that=2, yo_mama='fat')
s.read()

test_cases = {
    'arguments': 'data',
    'cases': [
        (t1, t2),
        (t1, t3),
        (t1, t2, t3),
    ]
}


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_init(data):
    Stack(
        data=data
    )


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_execute(data):
    o = Stack(
        data=data
    )
    o.execute()
