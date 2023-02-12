"""
This file gets the 3rd option.
"""
import csv
from datetime import date
from pandas import read_csv
from functools import reduce

FILE_NAMES = []
PHOTO = "{}.jpg|{}_{}_Proof.jpg"
VIDEO =  '{}_{}_'
sku_list = []
sku_letters = "r"

def _date():    # to get today's date
    today = date.today()
    d1 = today.strftime("%d%m20%y")
    return d1

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


def get_f_for_2nd_csv(FILE_NAMES):
    ret_list = []
    if len(FILE_NAMES)%2 == 0:
        half = int(len(FILE_NAMES)/2)
        for _ in range(1,(half+1)):
            ret_list.append(24)
        ret_list.append(8)
        while len(ret_list) != len(FILE_NAMES):
            ret_list.append('')
        return ret_list
    else:
        half = int((len(FILE_NAMES)+1)/2)
        for _ in range(1,(half+1)):
            ret_list.append(24)
        ret_list.append(8)
        while len(ret_list) != len(FILE_NAMES):
            ret_list.append('')
        return ret_list

def option_3(FILE_NAMES):
    product_list  = []
    price = []
    Sale_price = []
    photo_list = []
    video_list = []
    name_list = []
    name_link = []

    product_name = "{} {} signed model 8x10 Photo -PROOF- -CERTIFICATE- (A{})"
    date1 = _date()

    for i in FILE_NAMES:
        file_ele = i.split('_')
        First_name = file_ele[0].title()    # This extracts the first element
        Last_name = file_ele[1].title()     # This extracts the last element
        Last_4 = file_ele[-1]

        # product list
        product_list.append(product_name.format(First_name,Last_name,Last_4))
        
        #sku list
        sku = First_name + Last_name[0] + f"{Last_4}" + date1 + "r"
        sku_list.append(sku)

         # price
        price.append(29.95)

        # sale price
        Sale_price.append(22.95)

        # photo list
        photo_list.append(PHOTO.format(i, First_name, Last_name))
        
        # video list
        video_list.append('[video width="360" height="640" mp4="https://stalicali.com/wp-content/uploads/wpallimport/files/' + VIDEO.format(First_name, Last_name) + 'Signing_Autographs_Video.mp4"][/video]')

        # name list
        name_list.append((First_name+" "+Last_name))

        # namelink list
        name_link.append((First_name+"-"+Last_name))

    return [product_list, sku_list, price, Sale_price, photo_list, video_list, name_list, name_link]

def option_3_2nd_csv(FILE_NAMES, inventory_csv_path):
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
    column_f = get_f_for_2nd_csv(FILE_NAMES)
    # column_g = []
    last_sku =[]
    name_list = []


    product_name = "{} {} signed model 8x10 Photo -PROOF- -CERTIFICATE- (A{})"    
    date1 = _date()
    
    for i in FILE_NAMES:
        file_ele = i.split('_')
        First_name = file_ele[0].title()    # This extracts the first element
        Last_name = file_ele[1].title()     # This extracts the second element
        Last_4 = file_ele[-1]

        # name
        product_list.append(product_name.format(First_name,Last_name, Last_4))

        # sku list
        sku = First_name + Last_name[0] + f"{Last_4}" + date1 + "r"
        sku_list.append(sku)
         
        # price
        price.append(29.95)

        # column d
        column_d.append(1)

        # column e - skip all
        column_e.append("")

        # sku last part
        last_sku.append("r")

        # name list for col G
        name_list.append((First_name+" "+Last_name))

    column_g = col_g(col_G, col_H, col_I, name_list)
    return [product_list, sku_list, price, column_d, column_e, column_f, column_g, last_sku]

def option_3_3rd_csv(FILE_NAMES):
    column_f = get_f_for_2nd_csv(FILE_NAMES)
    column_a = []
    column_b = []

    for index,_ in enumerate(FILE_NAMES):
        # column a
        column_a.append(1)

        # column b
        if "" != column_f[index]:
            column_b.append(sku_list[index])
    return ([column_a, column_b])
