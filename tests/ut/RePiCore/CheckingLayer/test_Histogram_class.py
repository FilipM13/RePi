import pytest

from RePiCore.CheckingLayer.base import Histogram

test_cases = {
    'arguments': 'x, name, color',
    'cases': [
        (
            [1, 2, 3, 4, 1, 1, 1, 1, 2, 2, 3, 4, 1, 1, 1, 2, 2, 2, 3, 4, 1, 1, 1, 2],
            'random histogram',
            '#77ff00'
        )
    ]
}


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_init(x, name, color):
    Histogram(
        x=x,
        name=name,
        color=color
    )


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_render(x, name, color):
    o = Histogram(
        x=x,
        name=name,
        color=color
    )
    o.render()
