import pytest
import pandas as pd

from RePiCore.OperationLayer.base import Merge
from RePiCore.InputLayer.base import TableLike, SingleValues

t2 = TableLike(pd.DataFrame({
    'col1': [1, 2, 3, 4, 1, 1, 1, 1],
    'col2': [2, 2, 3, 4, 1, 1, 1, 2]
}))

t1 = TableLike(pd.DataFrame({
    'col1': [1, 2, 3, 4, 1, 1, 1, 1],
    'col2': [2, 2, 3, 4, 1, 1, 1, 2],
    'col3': [2, 2, 3, 4, 1, 1, 1, 2],
    'col4': [2, 2, 3, 4, 1, 1, 1, 2],
}))

s = SingleValues(this=1, that=2, yo_mama='fat')
s.read()

test_cases = {
    'arguments': 'data1, data2, on, how',
    'cases': [
        (t1, t2, 'col1', 'left'),
        (t1, t2, 'col2', 'right'),
        (t1, t2, 'col1', 'inner'),
        (t1, t2, 'col2', 'outer'),
        (t1, t2, 'col1', 'cross')
    ]
}


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_init(data1, data2, on, how):
    Merge(
        data1=data1,
        data2=data2,
        on=on,
        how=how
    )


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_execute(data1, data2, on, how):
    o = Merge(
        data1=data1,
        data2=data2,
        on=on,
        how=how
    )
    o.execute()
