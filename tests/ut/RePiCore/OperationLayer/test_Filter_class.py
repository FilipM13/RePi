import pytest
import pandas as pd

from RePiCore.OperationLayer.base import Filter
from RePiCore.InputLayer.base import TableLike, SingleValues

t = TableLike(pd.DataFrame({
    'col1': [1, 2, 3, 4, 1, 1, 1, 1],
    'col2': [2, 2, 3, 4, 1, 1, 1, 2]
}))
s = SingleValues(this=1, that=2, yo_mama='fat')
s.read()

test_cases = {
    'arguments': 'data, values, filters',
    'cases': [
        (t, s, {'col1': lambda x, sv: x == sv.this}),
        (t, s, {'col1': lambda x, sv: x == sv.this, 'col2': lambda x, sv: x == sv.that}),
    ]
}


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_init(data, values, filters):
    Filter(
        data=data,
        values=values,
        filters=filters
    )


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_execute(data, values, filters):
    o = Filter(
        data=data,
        values=values,
        filters=filters
    )
    o.execute()
