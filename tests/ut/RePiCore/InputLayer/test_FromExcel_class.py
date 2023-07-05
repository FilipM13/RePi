import pytest
from RePiCore.InputLayer.base import FromExcel

test_cases = {
    'arguments': 'path, sheet',
    'cases': [
        ('tests/data/data_sources/excel/1.xlsx', None),
        ('tests/data/data_sources/excel/2.xlsx', 'sheet2'),
    ]
}


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_init(path, sheet):
    FromExcel(path, sheet)


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_read(path, sheet):
    o = FromExcel(path, sheet)
    o.read()
