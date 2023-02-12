"""
This file gets the 7th option.
"""
import os
import csv
from datetime import date
import pandas as pd
from pandas import read_csv
from functools import reduce

FILE_NAMES = []
PHOTO = "{}.jpg|{}_{}_Proof.jpg|{}_{}_Proof.jpg"
VIDEO =  '{}_{}_'
sku_letters = "tsrc"
sku_list = []


def _date():    # to get today's date
    today = date.today()
    d1 = today.strftime("%d%m20%y")
    return d1

def write_list_to_csv_column(files, folder_path):
    pd.DataFrame({'product_name':files[0],
                'sku':files[1],
                'price':files[2],
                'Sale_price':files[3],
                'photos':files[4],
                'video':files[5],
                'name':files[6],
                'name-link':files[7],
                'name2':files[8],
                'name2link':files[9]}).to_csv(os.path.join(folder_path,'trans Combo2.csv'), index=False)
    print("csv written...")


def col_g(col_G, col_H, col_I, names):
    ret_list = ["" for _ in names]

    # remove the doubles from list
    particular_names = reduce(lambda re, x: re+[x] if x not in re else re, names, [])

    # Getting random numbers to use for non matches
    non_present_numbers_in_col_G = []
    for i in range(1, max(col_G)+10):
        if i not in col_G:
            non_present_numbers_in_col_G.append(i)
        if len(non_present_numbers_in_col_G) == len(particular_names):
            break

    matching_names = []
    names_in_inventory_col_H_with_index = []
    for name in particular_names:
        # Getting matching names and their index
        for index,lower_col_H in enumerate(col_H):
            if (name.lower() == lower_col_H.lower() 
                and col_I[index].lower() == sku_letters.lower()): # and name not in names_in_inventory_col_H_with_index 
                names_in_inventory_col_H_with_index.append([name,col_G[index]])
                matching_names.append(name)

    # Getting non matching name & index
    for i in particular_names:
        if i in matching_names:
            particular_names.remove(i)

    for name in particular_names:
        names_in_inventory_col_H_with_index.append([name, non_present_numbers_in_col_G[0]])
        non_present_numbers_in_col_G.pop(0)

    # remvoing duplicates from names_in_inventory_col_H_with_index
    temp_list = []
    for i in names_in_inventory_col_H_with_index:
        if i not in temp_list:
            temp_list.append(i)
    names_in_inventory_col_H_with_index = temp_list

    # Creating the return list by checking the matches and non matches
    if len(names_in_inventory_col_H_with_index) == 0:
        names_in_inventory_col_H_with_index = [[names[0],non_present_numbers_in_col_G[0]]]
        non_present_numbers_in_col_G.remove(non_present_numbers_in_col_G[0])

    namex = []
    result = []
    for sublist in names_in_inventory_col_H_with_index:
        name = sublist[0]
        if name not in namex:
            namex.append(name)
            result.append(sublist)

    # Making the return list
    for index,name in enumerate(names):
        for i in result:
            if name.lower().strip() == i[0].lower().strip():
                ret_list[index] = i[1]

    return (ret_list)


def option_7(FILE_NAMES, csv_folder_path):
    product_list  = []
    price = []
    Sale_price = []
    photo_list = []
    video_list = []
    name_list = []
    name_link = []
    name2_list = []
    name2_link = []

    product_name = "{} {} & {} {} signed TS model 8x10 Photo -PROOF- (A{})"
    date1 = _date()

    for i in FILE_NAMES:
        file_ele = i.split('_')
        First_name = file_ele[0].title()    # This extracts the first name element
        Last_name = file_ele[1].title()     # This extracts the 2nd name element
        third_name = file_ele[2].title()    # This extracts the 3rd name in the file
        fourth_name = file_ele[3].title()    # This extracts the 4th name in the file
        Last_4 = file_ele[-1]

        # product list
        product_list.append(product_name.format(First_name, Last_name, third_name, fourth_name, Last_4))
        
        #sku list
        sku = First_name + Last_name[0] + f"{Last_4}" + date1 + "tsrc"  # The end of sku
        sku_list.append(sku)

         # price
        price.append(94.95)

        # sale price
        Sale_price.append(74.95)

        # photo list
        photo_list.append(PHOTO.format(i, First_name, Last_name, third_name, fourth_name))
        
        # video list
        video_list.append('[video width="360" height="640" mp4="https://stalicali.com/wp-content/uploads/wpallimport/files/' + VIDEO.format(First_name, Last_name) + 'Signing_Autographs_Video.mp4"][/video]')

        # name list
        name_list.append((First_name+" "+Last_name))

        # namelink list
        name_link.append((First_name+"-"+Last_name))

        # name2 list
        name2_list.append(third_name+ " " +fourth_name)

        # name2 link
        name2_link.append(third_name+ "-" +fourth_name)

    write_list_to_csv_column([product_list, sku_list, price, Sale_price, photo_list, video_list, name_list, name_link, name2_list, name2_link],
        folder_path=csv_folder_path)


def option_7_2nd_csv(FILE_NAMES, inventory_csv_path):
    '''
    This option creates returns data for 2nd csv.
    '''
    with open(inventory_csv_path, "r") as file:
        data = list(csv.reader(file))
    colData = read_csv(inventory_csv_path) # read inventory
    data1 = data[0]
    col_G = colData[data1[6]].tolist() # inventory numbers col
    col_H = colData[data1[7]].tolist() # names columns
    col_I = colData[data1[8]].tolist() # sku columns
    product_list = []
    sku_list = []
    price =[]
    column_d = []
    column_e = []
    column_f = []
    last_sku =[]
    name_list = []

    product_name = "{} {} signed TS model B 8x10 Photo -PROOF- -CERTIFICATE- (A{})"
    date1 = _date()
    
    for i in FILE_NAMES:
        file_ele = i.split('_')
        First_name = file_ele[0].title()    # This extracts the first element
        Last_name = file_ele[1].title()     # This extracts the second element
        Last_4 = file_ele[-1]

        # name
        product_list.append(product_name.format(First_name,Last_name, Last_4))

        # sku list
        sku = First_name + Last_name[0] + f"{Last_4}" + date1 + "tsrc"
        sku_list.append(sku)
         
        # price
        price.append(29.95)

        # column d
        column_d.append(1)

        # column e
        column_e.append("")

        # column f
        column_f.append(38)

        # sku last part
        last_sku.append("tsrc")

        # name-list part
        name_list.append((First_name+" "+Last_name))

    column_g = col_g(col_G, col_H, col_I, name_list)
    return [product_list, sku_list, price, column_d, column_e, column_f, column_g, last_sku]

def option_7_3rd_csv(FILE_NAMES):
    column_a = []

    for _ in FILE_NAMES:
        # column a
        column_a.append(1)

    return ([column_a, sku_list])
