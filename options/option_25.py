"""
This file gets the 25th option. (back to one name only)
"""
import os
from datetime import date
import csv
from itertools import groupby, count
import pandas as pd
from pandas import read_csv
from functools import reduce

FILE_NAMES = []
PHOTO = "https://american-autographs.com/toimages//{}.jpg|"
VIDEO =  '{}_{}_'
sku_list = []
sku_letters = "RPR"
name_list = []
product_list_length = 0

def _date():    # to get today's date
    today = date.today()
    d1 = today.strftime("%d%m20%y")
    return d1

date1 = _date()

def write_list_to_csv_column(files, csv_folder_path):
    d = dict({'product_name':files[0],
                'sku':files[1],
                'price':files[2],
                'stock':files[3],
                'photos':files[4],
                'column f':files[5],
                'column g':files[6],
                'name':files[7]})
    pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in d.items() ])).to_csv(os.path.join(csv_folder_path,'RP porn REG.csv'),index=False)

    print("csv written...")

def col_f(colData, _sku, names, max, inventory_csv_path):
    with open(inventory_csv_path, "r") as file:
        data = list(csv.reader(file))
    data1 = data[0]
    app_list = []
    ret = []
    col_I = colData[data1[8]].tolist()
    col_H = colData[data1[7]].tolist()
    
    # gets all unique elemnts of list
    for _ in range(len(col_I)):
        app_list.append('')
    names = reduce(lambda re, x: re+[x] if x not in re else re, names, [])
    
    for name in names:
        sku_index = []
        name_index = []
        for idx, value in enumerate(col_I):  # type: ignore
            if value.lower() == _sku.lower():
                sku_index.append(idx)
        for idx, value in enumerate(col_H):
            if(value.lower() == name.lower()):
                name_index.append(idx)

        match = list(set(sku_index).intersection(name_index))
        match.sort()
        # print("match - ", match)

        # sorts the start and end of data - of all matches.
        c = count()
        result = [list(g) for i, g in groupby(match, key=lambda x: x-next(c))]
        for i in result:
            ret.append([i[0],i[-1]])


        for i in ret:
            for j in i:
                app_list[j] = 24

    return(app_list[:max])

def col_g(colData, _sku, names, max, inventory_csv_path):
    with open(inventory_csv_path, "r") as file:
        data = list(csv.reader(file))
    data1 = data[0]
    colData = read_csv(inventory_csv_path)
    col_G = colData[data1[6]].tolist()
    col_H = colData[data1[7]].tolist()
    col_I = colData[data1[8]].tolist()
    name_index = []
    g_index = []
    sku_index = []
    for name in names:
        for idx, value in enumerate(col_H): 
            if(value.lower() == name.lower()):
                name_index.append(idx)
        for idx, value in enumerate(col_I):
            if(value.lower() == _sku.lower()):
                sku_index.append(idx)
        match = list(set(name_index).intersection(sku_index))
        
        for idx, value in enumerate(col_G):
            g_index.append(idx)
        match = list(set(g_index).intersection(match))
        # print(match)
    
        match_g = []
        for _ in range(len(col_G)):
            match_g.append("")
        corresponding_values = [col_G[i] for i in match]
        for index, i in enumerate(match):
            match_g[i] = int(corresponding_values[index])
        # print(match_g)
        
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
                
        return (match_g[:max])

def option_25(FILE_NAMES, csv_folder_path, inventory_csv_path):
    colData = read_csv(inventory_csv_path) # read inventory
    product_list  = []
    price = []
    column_f = []
    stock = []
    photo = []

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
    
    global product_list_length
    product_list_length = int(len(product_list))
    column_f = col_f(colData, sku_letters, name_list, len(product_list),inventory_csv_path=inventory_csv_path)
    column_g = col_g(colData, sku_letters, name_list, len(product_list),inventory_csv_path=inventory_csv_path)

    write_list_to_csv_column([product_list, sku_list, price, stock, photo, column_f, column_g, name_list], csv_folder_path=csv_folder_path)

def option_25_3rd_csv(FILE_NAMES, inventory_csv_path):
    column_a = []
    column_b = []
    sku_2 = []
    colData = read_csv(inventory_csv_path) # read inventory
    column_f = col_f(colData, sku_letters, name_list, product_list_length, inventory_csv_path=inventory_csv_path)
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

    for i in range(product_list_length):
        if column_f[i] == 24:
            try:
                column_b.append(sku_2[i])
            except:
                column_b.append("")
        else:
            column_b.append("")

    return [column_a, column_b[:product_list_length]]
