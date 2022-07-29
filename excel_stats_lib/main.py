# ---- Open excel sheet ----
import excel_utilities as eu
import stats_proc as sp
# File path to test the code: E:\DEV\excel_stats\data\soundnames-LTM coordinates.xlsx
inputfile = "E:\DEV\excel_stats\data\soundnames-LTM coordinates.xlsx"

sheet = eu.getExcelSheet(inputfile)

col_names = eu.getSheetNames(sheet)

row_names = eu.getSheetNames(sheet, True)

data_list_col = eu.getDataList(sheet)

data_list_row = eu.getDataList(sheet, True)

data_dict = eu.getDataDict(sheet, col_names, data_list_row)

mean = sp.arithMean_col('L', col_names, data_list_col)

median = sp.median('L', col_names, data_list_col)

stat_mode = sp.stat_mode('L', col_names, data_list_col)
