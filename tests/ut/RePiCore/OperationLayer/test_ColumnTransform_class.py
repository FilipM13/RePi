import pytest
import pandas as pd

from RePiCore.OperationLayer.base import ColumnTransform
from RePiCore.InputLayer.base import TableLike, SingleValues

t1 = TableLike(pd.DataFrame({
    'col1': [1, 2, 3, 4, 1, 1, 1, 1],
    'col2': [2, 2, 3, 4, 1, 1, 1, 2]
}))

s = SingleValues(this=1, that=2, yo_mama='fat')
s.read()

test_cases = {
    'arguments': 'data',
    'cases': [
        (t1)
    ]
}


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_init(data):
    ColumnTransform(
        data=data
    )


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_execute(data):
    o = ColumnTransform(
        data=data
    )
    with pytest.raises(NotImplementedError):
        o.execute()
