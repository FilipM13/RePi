import pytest
from RePiCore.CheckingLayer.base import Graph, Scatter, Bar

test_cases = {
    'arguments': 'name, series',
    'cases': [
        (
            'Graph 1. you = f(fat)',
            [
                Scatter([1, 2, 3], [4, 5, 6], 'random', 'lines', '#ff0000'),
                Bar(['a1', 'b2', 'c3'], [4, 5, 6], 'random bar', '#ff0000'),
            ]
        )
    ]
}


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_init(name, series):
    Graph(name, series)


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_render(name, series):
    o = Graph(name, series)
    o.render()
