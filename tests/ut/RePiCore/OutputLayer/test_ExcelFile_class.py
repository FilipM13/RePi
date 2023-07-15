import pandas as pd
import pytest
import os

from RePiCore.OuputLayer.base import ExcelFile
from RePiCore.InputLayer.base import TableLike

table = TableLike(pd.DataFrame(
    {
        'this': ['1', '2', '3', '4', '5', '6'],
        'is': [1, 2, 3, 4, 5, 6],
        'test': ['2023-07-15', '2023-07-16', '2023-07-17', '2023-07-18', '2023-07-19', '2023-07-20'],
        'table': [True, False, True, False, True, False],
    }
))

scatter = TableLike(pd.DataFrame(
    {
        'x data': [0, 0, 9, 9, 6, 6],
        'y data 1': [1, 2, 3, 4, 5, 6],
        'y data 2': [6, 5, 4, 3, 2, 1],
    }
))


test_cases = {
    'arguments': 'file_name, tables, sheet_names',
    'cases': [
        ('test.xlsx', [table], None),
        ('test.xlsx', [table], ['table']),
        ('test.xlsx', [table, scatter], ['table', 'scatter']),
    ]
}


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_init(file_name, tables, sheet_names):
    ExcelFile(file_name, tables, sheet_names)


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_generate(file_name, tables, sheet_names):
    o = ExcelFile(file_name, tables, sheet_names)
    o.generate()
    os.remove(file_name)
