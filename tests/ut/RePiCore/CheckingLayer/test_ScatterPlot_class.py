import pytest
import pandas as pd

from RePiCore.CheckingLayer.base import ScatterPlot
from RePiCore.InputLayer.base import TableLike

t = TableLike(pd.DataFrame({
    'col1': [1, 2, 3, 4, 1, 1, 1, 1],
    'col2': [2, 2, 3, 4, 1, 1, 1, 2],
    'col3': [2, 2, 3, 4, 1, 1, 1, 2],
}))

test_cases = {
    'arguments': 'data, series, colors',
    'cases': [
        (t, [('col1', 'col2')], ["(255,0,0,1)"]),
        (t, [('col1', 'col3')], None),
        (t, [], None),
    ]
}


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_init(data, series, colors):
    ScatterPlot(
        data=data,
        series=series,
        colors=colors
    )


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_create_element(data, series, colors):
    o = ScatterPlot(
        data=data,
        series=series,
        colors=colors
    )
    o.create_element()


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_render(data, series, colors):
    o = ScatterPlot(
        data=data,
        series=series,
        colors=colors
    )
    o.render()
