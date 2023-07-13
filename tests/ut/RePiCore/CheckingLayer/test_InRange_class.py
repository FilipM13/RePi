import pytest
from RePiCore.CheckingLayer.base import InRange

test_cases = {
    'arguments': 'name, checked_value, max_value, min_value, description, max_inclusive, max_exclusive',
    'cases': [
        ('name stuff', -1, 3, 0, '-1 in <0, 3>', True, True),
        ('name stuff', 0, 3, 0, '0 in <0, 3>', True, True),
        ('name stuff', 1, 3, 0, '1 in <0, 3>', True, True),
        ('name stuff', 2, 3, 0, '2 in <0, 3>', True, True),
        ('name stuff', 3, 3, 0, '3 in <0, 3>', True, True),
        ('name stuff', 4, 3, 0, '4 in <0, 3>', True, True),
        ('name stuff', -1, 3, 0, '-1 in (0, 3)', False, False),
        ('name stuff', 0, 3, 0, '0 in (0, 3)', False, False),
        ('name stuff', 1, 3, 0, '1 in (0, 3)', False, False),
        ('name stuff', 2, 3, 0, '2 in (0, 3)', False, False),
        ('name stuff', 3, 3, 0, '3 in (0, 3)', False, False),
        ('name stuff', 4, 3, 0, '4 in (0, 3)', False, False),
        ('name stuff', -1.8, 3, 0, '-1 in (0, 3)', False, False),
        ('name stuff', 0, 3.8, 0, '0 in (0, 3)', False, False),
        ('name stuff', 1, 3, 0.8, '1 in (0, 3)', False, False),
    ]
}


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_init(name, checked_value, max_value, min_value, description, max_inclusive, max_exclusive):
    InRange(name, checked_value, max_value, min_value, description, max_inclusive, max_exclusive)


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_check(name, checked_value, max_value, min_value, description, max_inclusive, max_exclusive):
    o = InRange(name, checked_value, max_value, min_value, description, max_inclusive, max_exclusive)
    o.check()
