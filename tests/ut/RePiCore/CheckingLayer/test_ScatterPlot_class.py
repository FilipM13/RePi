import pytest

from RePiCore.CheckingLayer.base import Scatter

test_cases = {
    'arguments': 'x, y, name, mode, color',
    'cases': [
        (
            [1, 2, 3, 4, 1, 1, 1, 1],
            [2, 2, 3, 4, 1, 1, 1, 2],
            'test series',
            'lines',
            '#ff9900'
        )
    ]
}


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_init(x, y, name, mode, color):
    Scatter(
        x=x,
        y=y,
        name=name,
        mode=mode,
        color=color
    )


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_render(x, y, name, mode, color):
    o = Scatter(
        x=x,
        y=y,
        name=name,
        mode=mode,
        color=color
    )
    o.render()
