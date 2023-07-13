import pytest
from RePiCore.CheckingLayer.base import WithCheck

test_cases = {
    'arguments': 'name, description',
    'cases': [
        ('aa', 'b'),
        ('aaaaa', None),
    ]
}


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_init(name, description):
    WithCheck(name, description)


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_check(name, description):
    o = WithCheck(name, description)
    with pytest.raises(NotImplementedError):
        o.check()
