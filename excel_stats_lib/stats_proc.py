# 1 Location
# 1.1 Arithmetic Mean


def arithMean_col(columnName, col_names, data_list_columns):
    col_name = col_names.index(columnName)
    max_r = len(data_list_columns[col_name])
    mean = sum(data_list_columns[col_name])/(max_r)

    return mean

# 1.2 median


def median(columnName, col_names, data_list_columns):
    col_name = col_names.index(columnName)
    sortedList = data_list_columns[col_name]
    sortedList.sort()
    m = len(sortedList)
    if m % 2 == 0:
        med = (sortedList[int(m/2-1)]+sortedList[int(m/2)])/2
    elif m % 2 == 1:
        med = (sortedList[int(m/2)])

    return med


# 1.3 mode
def unique(in_list):

    # initialize a null list
    unique_list = []

    # traverse for all elements
    for x in in_list:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    return unique_list


def stat_mode(columnName, col_names, data_list_columns):
    col_name = col_names.index(columnName)
    in_list = data_list_columns[col_name]
    unique_list = unique(in_list)
    unXindex = [0 for x in range(0, len(unique_list))]
    for x in in_list:
        for index, ux in enumerate(unique_list):
            if x == ux:
                unXindex[index] += 1
    print(unique_list, unXindex)
    mode_index = max(unXindex)
    mode = unique_list[mode_index]
    return mode
