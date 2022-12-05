from pandas import *
import csv
from itertools import groupby, count


def get_indices(col_I, col_H, _sku, _name):
    sku_indices = []
    name_index = []
    ret = []
    app_list = []
    for idx, value in enumerate(col_I):  # type: ignore
        if value == _sku:
            sku_indices.append(idx)
    for idx, value in enumerate(col_H):
        if(value.lower() == _name.lower()):
            name_index.append(idx)
    match = list(set(sku_indices).intersection(name_index))
    
    # sorts the start and end of data
    c = count()
    result = [list(g) for i, g in groupby(match, key=lambda x: x-next(c))]
    for i in result:
        ret.append([i[0],i[-1]])

    print(ret)
    for i in range(ret[-1][-1]+1):
        app_list.append('')

    for i in ret:
        for j in i:
            app_list[j] = 24

    return(app_list)

with open("sample inventory sheet(1).csv", "r") as file:
    data = list(csv.reader(file))

data1 = data[0]
colData = read_csv("sample inventory sheet(1).csv")
sku_letters = "xxx"
Full_name = "Abby Cross"
col_i = colData[data1[8]].tolist()
col_h = colData[data1[7]].tolist() # type: ignore
col_g = colData[data1[6]].to_list()

match_list = get_indices(col_i,col_h, sku_letters, Full_name)
print(match_list)

