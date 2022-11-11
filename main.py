"""
This is the main module of the project, option1 is done.
"""
import os
import sys
import pandas as pd
from datetime import date
from options import option_2

NUMBER_OF_ELEMENTS_PER_OPTION = [4]
# CSV_FIRST_ROW = ["product_name", "sku", "price", "Sale_price", "photo", "video", "name", "name-link"]
FILE_NAMES = []
PHOTO = "{}_{}_Proof.jpg|{}_{}_Proof.jpg"
VIDEO =  '{}_{}_'

def _date():    # to get today's date
    today = date.today()
    d1 = today.strftime("%d%m20%y")
    return d1

def get_all_file_names(source_path):
    for root, dirs, files in os.walk(source_path):
        for name in files:
            FILE_NAMES.append(os.path.splitext(name)[0])  # To get file names without extension
            FILE_NAMES.sort()

def write_list_to_csv_column_option_1(file_names):
    pd.DataFrame({'product_name':file_names[0],
                'sku':file_names[1],
                'photo':file_names[2],
                'video':file_names[3],
                'name':file_names[4],
                # 'video':file_names[6],
                # 'name':file_names[7],
                'namelink':file_names[5]}).to_csv('named xxx.csv', index=False)
    print("csv written...")

def option_1(FILE_NAMES):
    product_list  = []
    sku_list = []
    photo_list = []
    video_list = []
    name_list = []
    name_link = []

    product_name = "{} {} signed XXX 8�10 Photo -PROOF- -CERTIFICATE- (A{})"
    date1 = _date()

    for i in FILE_NAMES:
        file_ele = i.split('_')
        First_name = file_ele[0].title()    # This extracts the first element
        Last_name = file_ele[1].title()     # This extracts the last element
        Last_4 = file_ele[-1]

        # product list
        product_list.append(product_name.format(First_name,Last_name,Last_4))
        
        #sku list
        sku = First_name + Last_name[0] + f"{Last_4}" + date1 + "X"
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

def main(source, option_number):
    cwd = os.getcwd()
    source_path = os.path.join(cwd, source)
    get_all_file_names(source_path)

    if option_number == 1:
        write_list_to_csv_column_option_1(option_1(FILE_NAMES))
    if option_number == 2:
        option_2.write_list_to_csv_column_option_2(option_2.option_2(FILE_NAMES))

if __name__ == '__main__':
    args = sys.argv
    if len(args) != 3:
        raise Exception("Only pass the folder name.")
    
    source, option_number = args[1:]

    main(source, int(option_number))