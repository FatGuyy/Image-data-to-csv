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
sku_letters = "RPRB"
name_list = []
product_list_length = 0

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
                'name':files[7]}).to_csv(os.path.join(csv_folder_path,'RP porn REG boob.csv'),index=False)

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

def col_g(colData, names, inventory_csv_path):
    with open(inventory_csv_path, "r") as file:
        data = list(csv.reader(file))
    data1 = data[0]
    colData = read_csv(inventory_csv_path)
    ret_list = ["" for _ in names]
    col_G = colData[data1[6]].tolist() # inventory numbers col
    col_H = colData[data1[7]].tolist() # names columns
    col_I = colData[data1[8]].tolist() # sku columns

    # remove the doubles from list 
    particular_names = reduce(lambda re, x: re+[x] if x not in re else re, names, [])
    names_in_inventory_col_H_with_index = []
    for name in particular_names:

        # Matching the names and getting their index
        for index,lower_col_H in enumerate(col_H):
            if (name.lower() == lower_col_H.lower() 
                and col_I[index].lower() == sku_letters.lower() 
                and name not in names_in_inventory_col_H_with_index):
                names_in_inventory_col_H_with_index.append([name,col_G[index]])

    # Getting random numbers to use for non matches
    non_present_numbers_in_col_G = []
    for i in range(1, max(col_G)+10):
        if i not in col_G:
            non_present_numbers_in_col_G.append(i)

    # Creating the return list by checking the matches and non matches
    for index,name in enumerate(names):
        number = 0
        for i in names_in_inventory_col_H_with_index:
            if name == i[0]:
                ret_list[index] = i[1]
            else:
                another_number = 0
                current_name = names[index]
                while current_name == name:
                    try:
                        current_name = names[index + another_number]
                        ret_list[index + another_number ] = non_present_numbers_in_col_G[number]
                        another_number += 1
                    except:
                        break
                # number += 1
    # print(ret_list)
    return (ret_list)


def option_28(FILE_NAMES, csv_folder_path, inventory_csv_path):
    colData = read_csv(inventory_csv_path) # read inventory
    product_list  = []
    price = []
    column_f = []   
    stock = []
    photo = []
    product_name = "Model {} {} autographed RP 8x10 Photo RP{}"

    for i in FILE_NAMES:
        file_ele = i.split('_')
        First_name = file_ele[0].title()    # This extracts the first element
        Last_name = file_ele[1].title()     # This extracts the last element
        Last_4 = file_ele[-1]

        # product list
        product_list.append(product_name.format(First_name,Last_name,Last_4))
        
        #sku list
        sku = First_name + Last_name[0] + f"{Last_4}" + date1 + "RPRB"
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
    product_list_length = len(product_list)
    column_f = col_f(colData, sku_letters, name_list, len(product_list),inventory_csv_path=inventory_csv_path)
    column_g = col_g(colData, name_list, inventory_csv_path=inventory_csv_path)

    write_list_to_csv_column([product_list, sku_list, price, stock, photo, column_f, column_g, name_list], csv_folder_path=csv_folder_path)

def option_28_3rd_csv(FILE_NAMES, inventory_csv_path):
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
        sku = First_name + Last_name[0] + f"{Last_4}" + date1 + "RPRB"
        sku_2.append(sku)

        # column a
        column_a.append(1)

    for i in range(product_list_length):
        if column_f[i] == 24:
            try:
                column_b.append(sku_2[i])
            except:
                column_b.append('')
        else:
            column_b.append('')

    return ([column_a, column_b[:product_list_length]])
