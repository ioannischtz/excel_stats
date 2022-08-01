import pytest
import excel_utilities as eu
import stats_proc as sp

inputfile = "E:\DEV\excel_stats\data\pytestfile.xlsx"
sheet = eu.getExcelSheet(inputfile)

test_getSheetNames = [
    pytest.param(
        (sheet, False),
        ('id', 'instrument', 'T', 'L', 'M'),
        'Expected different output when calling "getSheetNames()" with sheet, False as input',
        id='test_getSheetNames_cols'),
    pytest.param(
        (sheet, True),
        ('id', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
         13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24),
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
        [
    )
]

@pytest.mark.parametrize('arguments,expected_output,fail_message', test_getDataList)
def test_getDataList(arguments, expected_output, fail_message):
    actual = eu.getDataList(*arguments)
    assert actual == expected_output, fail_message


# def test_getDataDict(arguments, expected_output, fail_message):
#     actual = eu.getDataDict(*arguments)
#     assert actual == expected_output, fail_message


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
