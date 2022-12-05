"""
This file gets the 25th option. (back to one name only)
"""
import os
from datetime import date
import csv
from itertools import groupby, count
import pandas as pd
from pandas import read_csv

with open("sample inventory sheet(1).csv", "r") as file:
    data = list(csv.reader(file))
FILE_NAMES = []
PHOTO = "https://american-autographs.com/toimages//{}.jpg|"
VIDEO =  '{}_{}_'
sku_list = []
sku_letters = "xxx"
Full_name = "Abby Cross"
data1 = data[0]

def _date():    # to get today's date
    today = date.today()
    d1 = today.strftime("%d%m20%y")
    return d1

date1 = _date()

def write_list_to_csv_column(files, csv_folder_path):
    pd.DataFrame({'product_name':files[0],
                'sku':files[1],
                'price':files[2],
                'stock':files[3],
                'photos':files[4],
                'column f':files[5],
                'column g':files[6],
                'name':files[7]}).to_csv(os.path.join(csv_folder_path,'RP porn REG.csv'),index=False)

    print("csv written...")

def col_f(colData, _sku, _name, max):
    sku_indices = []
    name_index = []
    ret = []
    app_list = []
    col_I = colData[data1[8]].head(max).tolist()
    col_H = colData[data1[7]].head(max).tolist()
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

    for i in range(max):
        app_list.append('')

    for i in ret:
        for j in i:
            app_list[j] = 24

    return(app_list)

def col_g(colData, _sku, _name, max):
    sku_indices = []
    name_index = []
    app_list = []
    col_G = colData[data1[6]].head(max).tolist()
    col_G.sort()
    test_list_for_G = range(col_G[0], col_G[-1]+1000000)
    col_I = colData[data1[8]].head(max).tolist()
    col_H = colData[data1[7]].head(max).tolist()
    for idx, value in enumerate(col_I):  # type: ignore
        if value == _sku:
            sku_indices.append(idx)
    for idx, value in enumerate(col_H):
        if(value.lower() == _name.lower()):
            name_index.append(idx)
    match = list(set(sku_indices).intersection(name_index))
    print(match)

    for i in range(max):
        app_list.append('')

    number_to_be_appended = None
    counter = 0
    test =[]
    while counter < len(match):
        for i in range(max):
            if test_list_for_G[i] != col_G[i] and test_list_for_G[i] not in test:
                test.append(test_list_for_G[i])
                counter+=1
                break

    print(test)
    for i in match:
        j = test[i]
        app_list[i] = j
        # break

    # sorts the start and end of data
    # c = count()
    # result = [list(g) for i, g in groupby(match, key=lambda x: x-next(c))]
    # for i in result:
    #     ret.append([i[0],i[-1]])

    return(app_list)


def option_25(FILE_NAMES, csv_folder_path, inventory_csv_path):
    colData = read_csv(inventory_csv_path) # read inventory
    product_list  = []
    price = []
    stock = []
    photo = []
    name_list = []

    product_name = "{} {} autographed Model RP 8×10 Photo RP{}"

    for i in FILE_NAMES:
        file_ele = i.split('_')
        First_name = file_ele[0].title()    # This extracts the first element
        Last_name = file_ele[1].title()     # This extracts the last element
        Last_4 = file_ele[-1]

        # product list
        product_list.append(product_name.format(First_name,Last_name,Last_4))
        
        #sku list
        sku = First_name + Last_name[0] + f"{Last_4}" + date1 + "RPR"
        sku_list.append(sku)

         # price
        price.append(9.99)

        # sale price
        stock.append(1)

        # photo list
        photo.append(PHOTO.format(i))

        # name list
        name_list.append((First_name+" "+Last_name))

    column_f = col_f(colData, sku_letters, Full_name, len(product_list))
    column_g = col_g(colData, sku_letters, Full_name, len(product_list))


    write_list_to_csv_column([product_list, sku_list, price, stock, photo, column_f, column_g, name_list], csv_folder_path=csv_folder_path)

def option_25_3rd_csv(FILE_NAMES, inventory_csv_path):
    column_a = []
    column_b = []
    sku_2 = []
    colData = read_csv(inventory_csv_path) # read inventory
    column_f = col_f(colData, sku_letters, Full_name, len(FILE_NAMES))
    for i in FILE_NAMES:
        file_ele = i.split('_')
        First_name = file_ele[0].title()    # This extracts the first element
        Last_name = file_ele[1].title()     # This extracts the last element
        Last_4 = file_ele[-1]

        # getting sku
        sku = First_name + Last_name[0] + f"{Last_4}" + date1 + "RPR"
        sku_2.append(sku)

        # column a
        column_a.append(1)

    for i in range(len(column_f)):
        if column_f[i] == 24:
            column_b.append(sku_2[i])
        else:
            column_b.append('')

    return ([column_a, column_b])
