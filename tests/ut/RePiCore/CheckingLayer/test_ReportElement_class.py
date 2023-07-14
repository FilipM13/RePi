import pytest
from RePiCore.CheckingLayer.base import ReportElement

test_cases = {
    'arguments': 'template',
    'cases': [
        ('aa'),
        (None),
    ]
}


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_init(template):
    ReportElement(template)
