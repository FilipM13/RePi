import pytest
from RePiCore.CheckingLayer.base import Plain

test_cases = {
    'arguments': 'text, tag',
    'cases': [
        ('aaa', 'h1'),
        ('bbb', 'h2'),
        ('ccc', 'h3'),
        ('d', 'p'),
    ]
}


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_init(text, tag):
    Plain(text, tag)
