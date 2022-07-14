# 1.3 mode
def unique(list1):
 
    # initialize a null list
    unique_list = []
 
    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

def stat_mode(list1):
    unique_list = unique(list1)
    unXindex = [0 for x in range(0, len(unique_list))]
    for x in list1:
        for index,ux in enumerate(unique_list):
            if x == ux:
                unXindex[index] += 1
    mode_i = max(unXindex)
    mode_index = unXindex.index(mode_i)
    mode = unique_list[mode_index]
    return mode
qwerty = ["takis", "mitsos", "mitsos", "nikos"]
print(stat_mode(qwerty))