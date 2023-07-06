import pytest
from RePiCore.InputLayer.base import SingleValues

test_cases = {
    'arguments': 'd',
    'cases': [
        ({"key": 1, "k": 2, "e": 1.1, "y": True, "test": [True, "string", 1, 0, 1.111]}),
        ({}),
        ({"empty list": []}),
    ]
}


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_init(d):
    SingleValues(**d)


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_read(d):
    o = SingleValues(**d)
    o.read()


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_get_attributes(d):
    o = SingleValues(**d)
    o.read()
    o.get_values()
