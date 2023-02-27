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
column_f = []

def _date():    # to get today's date
    today = date.today()
    d1 = today.strftime("%d%m20%y")
    return d1

def col_g(col_G, col_H, col_I, names):
    ret_list = ["" for _ in names]

    # remove the doubles from list
    particular_names = list(set(names))

    # Getting non used numbers to use for non matches
    non_present_numbers_in_col_G = []
    for i in range(1, max(col_G)+1000):
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
    matching_names = list(set(matching_names))

    # Getting non matching name & index
    particular_names = [name for name in particular_names if name not in matching_names]
    # for i in particular_names:
    #     if i in matching_names:
    #         particular_names.remove(i)

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

def get_f_for_2nd_csv(names):
    ret_list = ['' for _ in range(len(names))]
    particular_names = list(set(names))
    list_with_start_and_end_index = []
    length = len(names)
    for j in particular_names:
        for index, val in enumerate(names):
            if j == val:
                app_lt = []
                # app_lt.append(int(j))
                app_lt.append(index)

                #loop for getting end index
                loop_itr = index
                try:
                    while j == names[loop_itr] and loop_itr <= length:
                        loop_itr += 1
                except:
                    pass
                app_lt.append(int(loop_itr-1))
                list_with_start_and_end_index.append(app_lt)
                break

    # print(list_with_start_and_end_index)
    # get the number of times for one name
    for i in list_with_start_and_end_index:
        if i[1]-i[0] == 0:
            ret_list[i[0]] = 24
        if i[1]-i[0] == 1:
            ret_list[i[0]] = 24
            ret_list[i[0]+1] = 8
        if i[1]-i[0] > 1:
            for j in range(int(int(i[1]-i[0])/2)):
                ret_list[i[0]+j] = 24
            ret_list[int(i[0]+((int(i[1]-i[0])/2)))] = 8

    # print(ret_list)
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

    global column_f
    column_f = get_f_for_2nd_csv(name_list)
    column_g = col_g(col_G, col_H, col_I, name_list)
    return [product_list, sku_list, price, column_d, column_e, column_f, column_g, last_sku]

def option_3_3rd_csv(FILE_NAMES):
    # column_f = get_f_for_2nd_csv(FILE_NAMES)
    column_a = []
    column_b = ["" for _ in FILE_NAMES]

    for index,_ in enumerate(FILE_NAMES):
        # column a
        column_a.append(1)

        # column b
        try:
            if "" != column_f[index]:
                column_b[index] = (sku_list[index])
        except:
            pass

    # print(column_b)
    return ([column_a, column_b])
