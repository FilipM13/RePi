import os

import RePiCore.InputLayer.base as IL
import RePiCore.OperationLayer.base as OL
import RePiCore.CheckingLayer.base as CL
import RePiCore.OuputLayer.base as RL


def test_scenario():
    # sources
    svs = IL.SingleValues(
        col1_upper_threshold=1,
        col2_lower_threshold=0,
        col3_lower_threshold=-1,
    )
    svs.read()
    in1 = IL.FromCsv('tests/data/scenarios/scenario1/in1.csv')
    in1.read()

    # operations
    filter1 = OL.Filter(in1, svs, filters={
        'col1': lambda x, sv: x < sv.col1_upper_threshold,
        'col2': lambda x, sv: x > sv.col2_lower_threshold,
        'col3': lambda x, sv: x > sv.col3_lower_threshold,
    }).execute()

    filter1_size = OL.Size(filter1).execute()

    matrix1 = OL.ColumnCompareMatrix(in1, column1='col2', column2='col3').execute()

    # checks
    header = CL.Plain('This is sample scenario1!', 'h1')
    size_check = CL.InRange('Size check', filter1_size['rows'], 50, 2)
    table_matrix = CL.Table(matrix1)
    filter_table = CL.Table(filter1, False)
    hist1 = CL.Histogram(in1, ['col1', 'col2'], ['(0,0,255,0.5)', '(255,0,0,0.5)'])

    # report
    html = RL.HtmlFile('Scenario 1.html', [
        header,
        size_check,
        filter_table,
        table_matrix,
        hist1
    ])
    excel = RL.ExcelFile('Scenario 1.xlsx', [filter_table, table_matrix], ['filtered shit', 'compared shit'])

    # rendering
    html.generate()
    excel.generate()
    os.remove('Scenario 1.xlsx')
    os.remove('Scenario 1.html')
