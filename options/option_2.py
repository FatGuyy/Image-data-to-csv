"""
This file gets the 2nd option.
"""
from datetime import date
import pandas as pd

FILE_NAMES = []
PHOTO = "{}_{}_Proof.jpg|{}_{}_Proof.jpg"
VIDEO =  '{}_{}_'

def write_list_to_csv_column_option_2(file_names):
    pd.DataFrame({'product_name':file_names[0],
                'sku':file_names[1],
                'photo':file_names[2],
                'video':file_names[3],
                'name':file_names[4],
                # 'video':file_names[6],
                # 'name':file_names[7],
                'namelink':file_names[5]}).to_csv('Reg Boob.csv', index=False)
    print("csv written...")

def _date():    # to get today's date
    today = date.today()
    d1 = today.strftime("%d%m20%y")
    return d1

def option_2(FILE_NAMES):
    product_list  = []
    sku_list = []
    photo_list = []
    video_list = []
    name_list = []
    name_link = []

    product_name = "{} {}signed model B 8�10 Photo -PROOF- -CERTIFICATE-  (A{})"
    date1 = _date()

    for i in FILE_NAMES:
        file_ele = i.split('_')
        First_name = file_ele[0].title()    # This extracts the first element
        Last_name = file_ele[1].title()     # This extracts the last element
        Last_4 = file_ele[-1]

        # product list
        product_list.append(product_name.format(First_name,Last_name,Last_4))
        
        #sku list
        sku = First_name + Last_name[0] + f"{Last_4}" + date1 + "rb"
        sku_list.append(sku)

        # photo list
        photo_list.append(PHOTO.format(First_name, Last_name, First_name, Last_name))
        
        # video list
        video_list.append('[video width="360" height="640" mp4="https://stalicali.com/wp-content/uploads/wpallimport/files/' + VIDEO.format(First_name, Last_name) + 'Signing_Autographs_Video.mp4"][/video]')

        # name list
        name_list.append((First_name+" "+Last_name))

        # namelink list
        name_link.append((First_name+"-"+Last_name))

    return [product_list, sku_list, photo_list, video_list, name_list, name_link]