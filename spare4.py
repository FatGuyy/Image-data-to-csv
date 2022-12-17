from pandas import *
import csv
def get_indices(_name, _sku):
    with open("sample inventory sheet(1).csv", "r") as file:
        data = list(csv.reader(file))
    data1 = data[0]
    colData = read_csv("sample inventory sheet(1).csv")
    col_G = colData[data1[6]].tolist()
    col_H = colData[data1[7]].tolist()
    col_I = colData[data1[8]].tolist()
    name_index = []
    g_index = []
    sku_index = [] 
    for idx, value in enumerate(col_H): 
        if(value.lower() == _name.lower()):
            name_index.append(idx)
    for idx, value in enumerate(col_I):
        if(value.lower() == _sku.lower()):
            sku_index.append(idx)
    match = list(set(name_index).intersection(sku_index))
    
    for idx, value in enumerate(col_G):
        g_index.append(idx)
    match = list(set(g_index).intersection(match))
    print(match)

    match_g = []
    for _ in range(len(col_G)):
        match_g.append("")
    corresponding_values = [col_G[i] for i in match]
    for index, i in enumerate(match):
        match_g[i] = int(corresponding_values[index])
    print(match_g)
    
    # getting the not in col G numbers
    col_G.sort()
    b = [x for x in range(col_G[0], col_G[-1] + 1)]
    a = set(col_G)
    not_in_col_G = list(a ^ set(b))

    counter_for_match_G = 0
    for i in not_in_col_G:
        if isinstance(match_g[counter_for_match_G], int):
            counter_for_match_G += 1
            if counter_for_match_G >= len(match_g):
                break 
        else:
            match_g[counter_for_match_G] = i
            counter_for_match_G += 1
            if counter_for_match_G >= len(match_g):
                break
    
    return (match_g)

name = "Abby Cross"
sku = "xxx"
get_indices(name, sku)