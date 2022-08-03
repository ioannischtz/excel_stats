# ---- Open excel sheet ----
import excel_utilities as eu
import stats_proc as sp
# File path to test the code: E:\DEV\excel_stats\data\pytestfile.xlsx
inputfile = "E:\DEV\excel_stats\data\pytestfile.xlsx"

sheet = eu.getExcelSheet(inputfile)


col_names = eu.getSheetNames(sheet)
# print(col_names)


row_names = eu.getSheetNames(sheet, True)
# print(row_names)

data_list_col = eu.getDataList(sheet)
# print(data_list_col)

data_list_row = eu.getDataList(sheet, True)
# print(data_list_row)

data_dict = eu.getDataDict(sheet, col_names, data_list_row)
# print(data_dict)

mean = sp.arithMean_col('LENGTH', col_names, data_list_col)
# print(mean)

median = sp.median('LENGTH', col_names, data_list_col)
# print(median)

stat_mode = sp.stat_mode('LENGTH', col_names, data_list_col)
print(stat_mode)