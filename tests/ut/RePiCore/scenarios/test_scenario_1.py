import os
import pandas as pd

import RePiCore.CheckingLayer.base as CL
import RePiCore.OuputLayer.base as RL


def test_scenario():
    df1 = pd.read_csv('tests/data/data_sources/csv/1.csv')
    df2 = pd.read_csv('tests/data/data_sources/csv/2.csv', sep=';')

    # checks
    header = CL.Plain('This is sample scenario1!', 'h1')
    size_check = CL.InRange('Size check', 10, 50, 2)
    table_matrix = CL.Table(df1)
    filter_table = CL.Table(df2, False)
    hist1 = CL.Histogram(
        df1['column1'].tolist(),
        'col1',
        '(0,0,255,0.5)'
    )

    # report
    html = RL.HtmlFile('Scenario 1.html', [
        header,
        size_check,
        filter_table,
        table_matrix,
        CL.Graph(
            'test g',
            [hist1]
        )
    ])
    excel = RL.ExcelFile('Scenario 1.xlsx', [filter_table, table_matrix], ['filtered shit', 'compared shit'])

    # rendering
    html.generate()
    excel.generate()
    os.remove('Scenario 1.xlsx')
    os.remove('Scenario 1.html')
