import pytest
from RePiCore.InputLayer.base import FromCsv

test_cases = {
    'arguments': 'path, delimiter, options',
    'cases': [
        ('tests/data/data_sources/csv/1.csv', ',', None),
        ('tests/data/data_sources/csv/2.csv', ';', {}),
        ('tests/data/data_sources/csv/3.csv', '$', {'parse_dates': ['column1']}),
    ]
}


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_init(path, delimiter, options):
    FromCsv(path=path, delimiter=delimiter, options=options)


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_read(path, delimiter, options):
    o = FromCsv(path=path, delimiter=delimiter, options=options)
    o.read()
