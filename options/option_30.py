"""
This file gets the 25th option. (back to one name only)
"""
import os
from datetime import date
import pandas as pd

FILE_NAMES = []
PHOTO = "https://american-autographs.com/toimages//{}.jpg|"
VIDEO =  '{}_{}_'

def _date():    # to get today's date
    today = date.today()
    d1 = today.strftime("%d%m20%y")
    return d1

def write_list_to_csv_column(files, csv_folder_path):
    pd.DataFrame({'product_name':files[0],
                'sku':files[1],
                'price':files[2],
                'stock':files[3],
                'photos':files[4],
                'column f':files[5],
                'column g':files[6],
                'name':files[7]}).to_csv(os.path.join(csv_folder_path,'RP porn Gay Reg.csv'),index=False)

    print("csv written...")

def option_30(FILE_NAMES, csv_folder_path):
    product_list  = []
    sku_list = []
    price = []
    stock = []
    photo = []
    column_f = []
    column_g = []
    name_list = []

    product_name = "{} {} autographed gay Model RP 8x10 Photo RP{}"
    date1 = _date()

    for i in FILE_NAMES:
        file_ele = i.split('_')
        First_name = file_ele[0].title()    # This extracts the first element
        Last_name = file_ele[1].title()     # This extracts the last element
        Last_4 = file_ele[-1]

        # product list
        product_list.append(product_name.format(First_name,Last_name,Last_4))
        
        #sku list
        sku = First_name + Last_name[0] + f"{Last_4}" + date1 + "RPG"
        sku_list.append(sku)

         # price
        price.append(9.99)

        # sale price
        stock.append(1)

        # photo list
        photo.append(PHOTO.format(i))

        # column f
        column_f.append('')
        
        # column g
        column_g.append('')        

        # name list
        name_list.append((First_name+" "+Last_name))

    write_list_to_csv_column([product_list, sku_list, price, stock, photo, column_f, column_g, name_list], csv_folder_path=csv_folder_path)

def option_30_3rd_csv(FILE_NAMES):
    column_a = []
    column_b = []
    for _ in FILE_NAMES:
        # column a
        column_a.append(1)

        # column b - waiting.
        column_b.append('')

    return ([column_a, column_b])
