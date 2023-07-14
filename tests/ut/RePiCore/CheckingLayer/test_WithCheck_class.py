import pytest
from RePiCore.CheckingLayer.base import WithCheck

test_cases = {
    'arguments': 'name, description, checked_value',
    'cases': [
        ('aa', 'b', 1),
        ('aaaaa', None, 1.0),
        ('aaaaa', None, '1.0'),
        ('aaaaa', None, True),
    ]
}


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_init(name, description, checked_value):
    WithCheck(name, description, checked_value)


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_check(name, description, checked_value):
    o = WithCheck(name, description, checked_value)
    with pytest.raises(NotImplementedError):
        o.check()
