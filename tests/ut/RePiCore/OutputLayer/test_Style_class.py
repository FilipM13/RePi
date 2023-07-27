import pytest

from RePiCore.OuputLayer.addons import Style


test_cases = {
    'arguments': 'border_color, hover_color, header_color, container_color, background_color',
    'cases': [
        ('#aaaaaa', '#aabbaa', '#000000', '#123456', '#ffffff'),
    ]
}


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_init(border_color, hover_color, header_color, container_color, background_color):
    Style(border_color, hover_color, header_color, container_color, background_color)
