import matplotlib.pyplot as plt
import excel_utilities as eu
import math


def graph_creator_func(inputfile):
    # Link with the excel file
    sheet = eu.getExcelSheet(inputfile)
    col_names = eu.getSheetNames(sheet)
    data_list_rows = eu.getDataList(sheet, b_rows=True)
    data_list_columns = eu.getDataList(sheet)
    data_dict = eu.getDataDict(sheet, col_names, data_list_rows)

    # Calculating the dimentions of the subplot matrix
    multitude = len(data_list_columns[1])

    dim = int(math.sqrt(multitude))
    if math.sqrt(multitude) == int(math.sqrt(multitude)):
        pass
    else:
        dim += 1

    new_list = []
    assist_list1 = []
    assist_list2 = []

    for i in range(0, len(data_list_rows)):
        assist_list1 = data_list_rows[i]
        for j in range(2, len(assist_list1)):
            assist_list2.append(assist_list1[j])
        new_list.append(assist_list2)
        assist_list1 = []
        assist_list2 = []

    # Matplotlib subplots
    ind_col_names = []
    for i, name in enumerate(col_names[2:]):
        ind_col_names.append(i+1)

    count_plot = 0
    fig, ax_array = plt.subplots(dim, dim, squeeze=False)
    for i, ax_row in enumerate(ax_array):
        for j, axes in enumerate(ax_row):
            if count_plot < multitude:
                titles = data_list_columns[1]

                axes.bar(ind_col_names, new_list[count_plot],
                         width=1, edgecolor="black", linewidth=1)
                axes.set(xlim=(0, len(new_list[count_plot])+1), ylim=(min(new_list[count_plot])-1, max(new_list[count_plot])+1),
                         title=titles[count_plot], xticks=ind_col_names, xticklabels=col_names[2:])

            if count_plot == multitude:
                axes.set_title('{},{}'.format(i, j))
                axes.set_yticklabels([])
                axes.set_xticklabels([])
            count_plot += 1

    plt.show()


# Calling the function test
# inputfile = 'E:\DEV\excel_stats\data\pytestfile.xlsx'
# graph_creator_func("E:\DEV\excel_stats\data\pytestfile.xlsx")
