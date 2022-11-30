"""
This file gets the 17th option.
"""
import os
from datetime import date
import pandas as pd

FILE_NAMES = []
PHOTO = "{}.jpg|{}_{}_Proof.jpg|{}_{}_Proof.jpg|{}_{}_Proof.jpg"
VIDEO =  '{}_{}_'
product_list  = []
sku_list = []

def _date():    # to get today's date
    today = date.today()
    d1 = today.strftime("%d%m20%y")
    return d1

def write_list_to_csv_column(files, csv_folder_path):
    pd.DataFrame({'product_name':files[0],
                'sku':files[1],
                'price':files[2],
                'Sale_price':files[3],
                'photos':files[4],
                'video':files[5],
                'name':files[6],
                'name-link':files[7],
                'name2':files[8],
                'name2link':files[9]}).to_csv(os.path.join
                        (csv_folder_path,
                        'reg boob Combo2.csv'),
                        index=False)

    print("csv written...")


def option_17(FILE_NAMES, csv_folder_path):
    price = []
    Sale_price = []
    photo_list = []
    video_list = []
    name_list = []
    name_link = []
    name2_list = []
    name2_link = []

    product_name = "{} {} & {} {} & {} {} signed model B 8×10 Photo -PROOF- (A{})"
    date1 = _date()

    for i in FILE_NAMES:
        file_ele = i.split('_')
        First_name = file_ele[0].title()    # This extracts the first element
        Last_name = file_ele[1].title()     # This extracts the last element
        third_name = file_ele[2].title()    # This extracts the 3rd name in the file
        fourth_name = file_ele[3].title()   # This extracts the 4th name in the file
        fifth_name = file_ele[4].title()    # This extracts the 5th name in the file
        sixth_name = file_ele[5].title()    # This extracts the 6th name in the file
        Last_4 = file_ele[-1]

        # product list
        product_list.append(product_name.format(First_name, Last_name, third_name, fourth_name, fifth_name, sixth_name, Last_4))
        
        #sku list
        sku = First_name + Last_name[0] + f"{Last_4}" + date1 + "rbc"  # The end of sku
        sku_list.append(sku)

         # price
        price.append(94.95)

        # sale price
        Sale_price.append(74.95)

        # photo list
        photo_list.append(PHOTO.format(i, First_name, Last_name, third_name, fourth_name, fifth_name, sixth_name))
        
        # video list
        video_list.append('[video width="360" height="640" mp4="https://stalicali.com/wp-content/uploads/wpallimport/files/' + VIDEO.format(First_name, Last_name) + 'Signing_Autographs_Video.mp4"][/video]')

        # name1 list
        name_list.append((First_name+" "+Last_name))

        # namelink1 list
        name_link.append((First_name+"-"+Last_name))

        # name2 list
        name2_list.append(third_name+ " " +fourth_name)

        # name2 link
        name2_link.append(third_name+ "-" +fourth_name)

    write_list_to_csv_column([product_list, sku_list, price, Sale_price, photo_list, video_list, name_list, name_link, name2_list, name2_link],
        csv_folder_path=csv_folder_path)

def option_17_2nd_csv(FILE_NAMES):
    '''
    This option creates returns data for 2nd csv.
    '''
    price =[]
    column_d = []
    column_e = []
    column_f = []
    column_g = []
    last_sku =[]        
    
    for _ in FILE_NAMES:         
        # price
        price.append(29.95)

        # column d
        column_d.append(1)

        # column e
        column_e.append("")

        # column f
        column_f.append(38)

        # column g
        column_g.append('')

        # sku last part
        last_sku.append("rbc")

    return [product_list, sku_list, price, column_d, column_e, column_f, column_g, last_sku]
