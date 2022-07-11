# ---- Open excel sheet ----
from openpyxl import load_workbook
# File path to test the code: E:\DEV\excel_stats\data\soundnames-LTM coordinates.xlsx
inputfile = "E:\DEV\excel_stats\data\soundnames-LTM coordinates.xlsx"


def extractExceldata(inputfile):
    wb = load_workbook(filename=inputfile)
    sheet = wb.active
    max_r = sheet.max_row
    max_c = sheet.max_column
    for names in sheet.iter_rows(min_row=1,
                                 max_row=1,
                                 values_only=True):
        col_names = names
    data = [[sheet.cell(row=i, column=j).value for j in range(
            1, sheet.max_column+1)] for i in range(2, sheet.max_row+1)]
    data_dict = {}
    for i, col_name in enumerate(col_names):
        data_dict[col_name] = [row[i] for row in data]
    return (col_names, data_dict, max_r, max_c)


# 1 Location
# 1.1 Arithmetic Mean


def arMean_col_i(columnName):
    col_names, data_dict, max_r, max_c = extractExceldata(inputfile)
    col_num = col_names.index(columnName)
    x = sum(data_dict[col_names[col_num]])/(max_r-1)
    print("The arithmetic mean of column '", columnName, "' is: ", x)
