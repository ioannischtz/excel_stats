# ---- Open excel sheet ----
from ctypes import sizeof
from openpyxl import load_workbook
wb = load_workbook(filename='./data/soundnames-LTM coordinates.xlsx')
sheet = wb.active

for names in sheet.iter_rows(min_row=1,
                             max_row=1,
                             values_only=True):
    col_names = names

# print(col_names)


# x = [[0 for i in range(10)] for j in range(10)]
# # x is now a 10x10 array of 'foo' (which can depend on i and j if you want)
# print(x)

data = [[0 for i in range(1, sheet.max_column + 1)]
        for j in range(2, sheet.max_row + 1)]

# print(len(data), len(data[0]))

for row_i in range(2, sheet.max_row + 1):
    for col_i in range(1, sheet.max_column + 1):
        data[row_i-2][col_i-1] = sheet.cell(row=row_i, column=col_i).value

# print(data)

data_dict = {}  # create an empty dictionary

for i, col_name in enumerate(col_names):
    data_dict[col_name] = [row[i] for row in data]

# print(col_names[1],data_dict[col_names[1]])
print('id:', data_dict['id'])
print('instrument:', data_dict['instrument'])
print('T:', data_dict['T'])
print('L:', data_dict['L'])
print('M', data_dict['M'])

# ---- perform statistical analysis ----

# 1 Location
# 1.1 arithmetic mean
# 1.2 median
# 1.3 mode
# 1.4 interquartile mean

# 2 Spread
# 2.1 std deviation
# 2.2 variance
# 2.3 range
# 2.4 interquartile range
# 2.5 absolute deviation
# 2.6 mean absolute difference
# 2.7 distance standard deviation
# 2.8 Gini coefficient

# 3 Shape
# 3.1 skewness

# 4 Dependence
# 4.1 Pearson product-moment correlation coefficient
# 4.2 Spearman's rank coreelatio ncoefficient

# ---- Visualize the results ----

# ---- Save the results to a file ----
