"""
This file gets the 5th option.
"""
import csv
from datetime import date
from pandas import read_csv
from functools import reduce

FILE_NAMES = []
PHOTO = "{}.jpg|{}_{}_Proof.jpg"
VIDEO =  '{}_{}_'
sku_list = []
sku_letters = "tsr"

def _date():    # to get today's date
    today = date.today()
    d1 = today.strftime("%d%m20%y")
    return d1

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
    if len(names_in_inventory_col_H_with_index) == 0:
        names_in_inventory_col_H_with_index = [[names[0],non_present_numbers_in_col_G[0]]]
        non_present_numbers_in_col_G.remove(non_present_numbers_in_col_G[0])
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

def option_5(FILE_NAMES):
    product_list  = []
    price = []
    Sale_price = []
    photo_list = []
    video_list = []
    name_list = []
    name_link = []

    product_name = "{} {} signed TS model 8x10 Photo -PROOF- -CERTIFICATE- (A{})"
    date1 = _date()

    for i in FILE_NAMES:
        file_ele = i.split('_')
        First_name = file_ele[0].title()    # This extracts the first element
        Last_name = file_ele[1].title()     # This extracts the last element
        Last_4 = file_ele[-1]

        # product list
        product_list.append(product_name.format(First_name,Last_name,Last_4))
        
        #sku list
        sku = First_name + Last_name[0] + f"{Last_4}" + date1 + "tsr"
        sku_list.append(sku)

         # price
        price.append(54.95)

        # sale price
        Sale_price.append(37.95)

        # photo list
        photo_list.append(PHOTO.format(i, First_name, Last_name))
        
        # video list
        video_list.append('[video width="360" height="640" mp4="https://stalicali.com/wp-content/uploads/wpallimport/files/' + VIDEO.format(First_name, Last_name) + 'Signing_Autographs_Video.mp4"][/video]')

        # name list
        name_list.append((First_name+" "+Last_name))

        # namelink list
        name_link.append((First_name+"-"+Last_name))

    return [product_list, sku_list, price, Sale_price, photo_list, video_list, name_list, name_link]

def option_5_2nd_csv(FILE_NAMES, inventory_csv_path):
    '''
    This option creates returns data for 2nd csv.
    '''
    colData = read_csv(inventory_csv_path) # read inventory
    product_list = []
    sku_list = []
    price =[]
    column_d = []
    column_e = []
    column_f = []
    last_sku =[]
    name_list = []

    product_name = "{} {} signed TS model 8x10 Photo -PROOF- -CERTIFICATE- (A{})"    
    date1 = _date()
    
    for i in FILE_NAMES:
        file_ele = i.split('_')
        First_name = file_ele[0].title()    # This extracts the first element
        Last_name = file_ele[1].title()     # This extracts the second element
        Last_4 = file_ele[-1]

        # name
        product_list.append(product_name.format(First_name,Last_name, Last_4))

        # sku list
        sku = First_name + Last_name[0] + f"{Last_4}" + date1 + "tsr"
        sku_list.append(sku)
         
        # price
        price.append(29.95)

        # column d
        column_d.append(1)

        # column e
        column_e.append("")

        # column f
        column_f.append(22)

        # column g
        # column_g.append('')

        # sku last part
        last_sku.append("tsr")

        # name list for col G
        name_list.append((First_name+" "+Last_name))

    column_g = col_g(colData, name_list, inventory_csv_path=inventory_csv_path)
    return [product_list, sku_list, price, column_d, column_e, column_f, column_g, last_sku]

def option_5_3rd_csv(FILE_NAMES):
    column_a = []

    for _ in FILE_NAMES:
        # column a
        column_a.append(1)

    return ([column_a, sku_list])
