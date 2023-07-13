import pytest
from RePiCore.CheckingLayer.base import Equals

test_cases = {
    'arguments': 'name, checked_value, expected_value, description',
    'cases': [
        ('name stuff', True, True, 'very description yes'),
        ('name stuff', True, False, 'very description yes'),
        ('name stuff', 1, 1, 'very description yes'),
        ('name stuff', 2, 1, 'very description yes'),
        ('name stuff', 1.001, 1, 'very description yes'),
        ('name stuff', 2.123165, 3416541, 'very description yes'),
        ('name stuff', '', 'eee', 'very description yes'),
        ('name stuff', 'nie', 'po', 'very description yes'),
        ('name stuff', 'sionym', 'sionym', None),
    ]
}


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_init(name, checked_value, expected_value, description):
    Equals(name, checked_value, expected_value, description)


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_check(name, checked_value, expected_value, description):
    o = Equals(name, checked_value, expected_value, description)
    o.check()
