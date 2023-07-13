import pytest
import pandas as pd

from RePiCore.OperationLayer.base import Rename, Order, Maintain, Drop
from RePiCore.InputLayer.base import TableLike, SingleValues

t1 = TableLike(pd.DataFrame({
    'col1': [1, 2, 3, 4, 1, 1, 1, 1],
    'col2': [2, 2, 3, 4, 1, 1, 1, 2],
    'col3': [2, 2, 3, 4, 1, 1, 1, 2],
    'col4': [2, 2, 3, 4, 1, 1, 1, 2],
    'col5': [2, 2, 3, 4, 1, 1, 1, 2],
    'col6': [2, 2, 3, 4, 1, 1, 1, 2],
}))

s = SingleValues(this=1, that=2, yo_mama='fat')
s.read()

test_cases = {
    'arguments': 'data, names, cls',
    'cases': [
        (t1, {'p1': 'col1', 'p3': 'col2', 'p5': 'col3'}, Rename),
        (t1, {'p1': 'col1'}, Rename),
        (t1, ['col1', 'col5', 'col6'], Order),
        (t1, ['col1'], Order),
        (t1, ['col1', 'col2'], Maintain),
        (t1, ['col3'], Maintain),
        (t1, ['col1', 'col2'], Drop),
        (t1, ['col3'], Drop),
    ]
}


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_init(data, names, cls):
    cls(
        data=data,
        names=names
    )


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_execute(data, names, cls):
    o = cls(
        data=data,
        names=names
    )
    o.execute()
