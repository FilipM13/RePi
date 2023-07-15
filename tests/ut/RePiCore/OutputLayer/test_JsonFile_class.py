import pandas as pd
import pytest
import os

from RePiCore.OuputLayer.base import JsonFile
from RePiCore.InputLayer.base import TableLike
from RePiCore.CheckingLayer.base import Table


scatter = Table(TableLike(pd.DataFrame(
    {
        'x data': [0, 0, 9, 9, 6, 6],
        'y data 1': [1, 2, 3, 4, 5, 6],
        'y data 2': [6, 5, 4, 3, 2, 1],
    }
)))


test_cases = {
    'arguments': 'file_name, table',
    'cases': [
        ('test.json', scatter),
    ]
}


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_init(file_name, table):
    JsonFile(file_name, table)


@pytest.mark.parametrize(
    test_cases['arguments'],
    test_cases['cases']
)
def test_generate(file_name, table):
    o = JsonFile(file_name, table)
    o.generate()
    os.remove(file_name)
