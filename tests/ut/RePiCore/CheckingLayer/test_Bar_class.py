import pytest

from RePiCore.CheckingLayer.base import Bar

test_cases = {
    'arguments': 'x, y, name, color',
    'cases': [
        (
            ['a1', 'a2', 'a3', 'a4', 'a5', 'a6'],
            [5, 9, 2, 0, -5, 10],
            'random bar',
            '#00ffaa'
        )
    ]
}


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_init(x, y, name, color):
    Bar(
        x=x,
        y=y,
        name=name,
        color=color
    )


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_render(x, y, name, color):
    o = Bar(
        x=x,
        y=y,
        name=name,
        color=color
    )
    o.render()
