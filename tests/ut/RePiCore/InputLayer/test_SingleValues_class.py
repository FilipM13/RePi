import pytest
from RePiCore.InputLayer.base import SingleValues


@pytest.mark.parametrize(
    'd',
    [
        ({'key': 1, 'k': 2, 'e': 1.1, 'y': True, 'test': [True, 'string', 1, 0, 1.111]}),
        ({}),
        ({'empty list': []})
    ]
)
def test_init(d):
    SingleValues(**d)
