# ---- Open excel sheet ----
import excel_utilities as eu
import stats_proc as sp
import graph_creator as gc

# File path to test the code: E:\DEV\excel_stats\data\pytestfile.xlsx
inputfile = "E:\DEV\excel_stats\data\pytestfile.xlsx"

sheet = eu.getExcelSheet(inputfile)
# print(sheet)

col_names = eu.getSheetNames(sheet)
# print(type(col_names))


row_names = eu.getSheetNames(sheet, True)
# print(row_names)

data_list_cols = eu.getDataList(sheet)
# print(type(data_list_col))

data_list_rows = eu.getDataList(sheet, True)
# print(data_list_row)

data_dict = eu.getDataDict(sheet, col_names, data_list_rows)
# print(data_dict)

mean = sp.arithMean_col('LENGTH', col_names, data_list_cols)
# print(type(mean))

median = sp.median('LENGTH', col_names, data_list_cols)
# print(median)

stat_mode = sp.stat_mode('LENGTH', col_names, data_list_cols)
# print(stat_mode)

gc.graph_creator_func(inputfile)