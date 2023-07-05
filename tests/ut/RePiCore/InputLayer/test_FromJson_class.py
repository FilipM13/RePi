import pytest
from RePiCore.InputLayer.base import FromJson

test_cases = {
    'arguments': 'path, per_line_regex, headers',
    'cases': [
        ('tests/data/data_sources/json/1.json', r'"title": "([a-zA-Z0-9\s\.]*)"', ['title']),
        ('tests/data/data_sources/json/1.json', r'"title": "([a-zA-Z0-9\s\.]*), "author": "([a-zA-Z0-9\s\.]*)""', ['title', 'author']),
        ('tests/data/data_sources/json/2.json', r'"title": "([a-zA-Z0-9\s\.]*)", "author": "([a-zA-Z0-9\s\.]*)"', ['title', 'author']),
        ('tests/data/data_sources/json/2.json', r'"title": "([a-zA-Z0-9\s\.]*)"', ['title']),
        ('tests/data/data_sources/json/3.json', r'"title": "([a-zA-Z0-9\s\.]*)", "author": "([a-zA-Z0-9\s\.]*)"', ['title', 'author']),
        ('tests/data/data_sources/json/3.json', r'"title": "([a-zA-Z0-9\s\.]*)"', ['title']),
    ]
}


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_init(path, per_line_regex, headers):
    FromJson(path, per_line_regex, headers)


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_read(path, per_line_regex, headers):
    o = FromJson(path, per_line_regex, headers)
    o.read()
