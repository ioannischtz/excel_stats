import pytest
import excel_utilities as eu
import stats_proc as sp

inputfile = "E:\DEV\excel_stats\data\pytestfile.xlsx"
sheet = eu.getExcelSheet(inputfile)

test_getSheetNames = [
    pytest.param(
        (sheet, False),
        ('ID', 'OBJECT', 'HEIGHT', 'LENGTH', 'WIDTH'),
        'Expected different output when calling "getSheetNames()" with sheet, False as input',
        id='test_getSheetNames_columns'),
    pytest.param(
        (sheet, True),
        ('ID', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
        'Expected different output when calling "getSheetNames()" with sheet, True as input',
        id='test_getSheetNames_rows')
]


@pytest.mark.parametrize('arguments,expected_output,fail_message', test_getSheetNames)
def test_getSheetNames(arguments, expected_output, fail_message):
    actual = eu.getSheetNames(*arguments)
    assert actual == expected_output, fail_message


test_getDataList = [
    pytest.param(
        (sheet, False),
        [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
         ['ob1', 'ob2', 'ob3', 'ob4', 'ob5', 'ob6', 'ob7', 'ob8', 'ob9', 'ob10'],
         [2, 3, 6, 5, 8, 2, 1, 3, 2, 6],
         [3, 1, 2, 6, 1, 4, 5, 5, 9, 4],
         [4, 6, 4, 1, 6, 7, 4, 2, 1, 5]],
        'Expected different output when calling "test_getDataList()" with sheet, False as input',
        id='test_getDataList_columns'),
    pytest.param(
        (sheet, True),
        [[1, 'ob1', 2, 3, 4],
         [2, 'ob2', 3, 1, 6],
         [3, 'ob3', 6, 2, 4],
         [4, 'ob4', 5, 6, 1],
         [5, 'ob5', 8, 1, 6],
         [6, 'ob6', 2, 4, 7],
         [7, 'ob7', 1, 5, 4],
         [8, 'ob8', 3, 5, 2],
         [9, 'ob9', 2, 9, 1],
         [10, 'ob10', 6, 4, 5]],
        'Expected different output when calling "test_getDataList()" with sheet, True as input',
        id='test_getDataList_rows')
]


@pytest.mark.parametrize('arguments,expected_output,fail_message', test_getDataList)
def test_getDataList(arguments, expected_output, fail_message):
    actual = eu.getDataList(*arguments)
    assert actual == expected_output, fail_message


test_getDataDict = [
    pytest.param(
        (sheet,
         ('ID', 'OBJECT', 'HEIGHT', 'LENGTH', 'WIDTH'),
         [[1, 'ob1', 2, 3, 4],
          [2, 'ob2', 3, 1, 6],
          [3, 'ob3', 6, 2, 4],
          [4, 'ob4', 5, 6, 1],
          [5, 'ob5', 8, 1, 6],
          [6, 'ob6', 2, 4, 7],
          [7, 'ob7', 1, 5, 4],
          [8, 'ob8', 3, 5, 2],
          [9, 'ob9', 2, 9, 1],
          [10, 'ob10', 6, 4, 5]]),
        {'ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
         'OBJECT': ['ob1', 'ob2', 'ob3', 'ob4', 'ob5', 'ob6', 'ob7', 'ob8', 'ob9', 'ob10'],
         'HEIGHT': [2, 3, 6, 5, 8, 2, 1, 3, 2, 6],
         'LENGTH': [3, 1, 2, 6, 1, 4, 5, 5, 9, 4],
         'WIDTH': [4, 6, 4, 1, 6, 7, 4, 2, 1, 5]},
        'Expected different output when calling "test_getDataDict()" with sheet as input',
        id='test_detDataDict')
]


def test_getDataDict(arguments, expected_output, fail_message):
    actual = eu.getDataDict(*arguments)
    assert actual == expected_output, fail_message


# def test_arithMean_col(arguments, expected_output, fail_message):
#     actual = sp.arithMean_col(*arguments)
#     assert actual == expected_output, fail_message


# def test_median(arguments, expected_output, fail_message):
#     actual = sp.median(*arguments)
#     assert actual == expected_output, fail_message


# def test_unique(arguments, expected_output, fail_message):
#     actual = sp.unique(*arguments)
#     assert actual == expected_output, fail_message


# def test_mode(arguments, expected_output, fail_message):
#     actual = sp.mode(*arguments)
#     assert actual == expected_output, fail_message
