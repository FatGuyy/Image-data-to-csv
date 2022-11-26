"""
This is the main module of the project, option1 is done.
"""
import os
import pandas as pd
from datetime import date
from options import (
        option_2,
        option_3,
        option_4, 
        option_5, 
        option_6, 
        option_7, 
        option_8, 
        option_9, 
        option_10, 
        option_11)


NUMBER_OF_ELEMENTS_PER_OPTION = [4]
# CSV_FIRST_ROW = ["product_name", "sku", "price", "Sale_price", "photo", "video", "name", "name-link"]
FILE_NAMES = []
PHOTO = "{}.jpg|{}_{}_Proof.jpg"
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

def write_list_to_csv_column(name_of_file, files, folder_path):
    df = pd.DataFrame({'product_name':files[0],
                'sku':files[1],
                'price':files[2],
                'Sale_price':files[3],
                'photos':files[4],
                'video':files[5],
                'name':files[6],
                'name-link':files[7]})
    df.to_csv(os.path.join(folder_path,(name_of_file + '.csv')), index=False)
    print("csv written...")

def option_1(FILE_NAMES):
    product_list  = []
    sku_list = []
    price = []
    Sale_price = []
    photo_list = []
    video_list = []
    name_list = []
    name_link = []

    product_name = "{} {} signed XXX 8×10 Photo -PROOF- -CERTIFICATE- (A{})"
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

def main(source, option_number, CSV_folder_path):
    cwd = os.getcwd()
    source_path = os.path.join(cwd, source)
    get_all_file_names(source_path)

    if option_number == 1:
        write_list_to_csv_column('xxx', option_1(FILE_NAMES), folder_path=CSV_folder_path)
    elif option_number == 2:
        write_list_to_csv_column('reg Boob', option_2.option_2(FILE_NAMES), folder_path=CSV_folder_path)
    elif option_number == 3:
        write_list_to_csv_column('REG', option_3.option_3(FILE_NAMES), folder_path=CSV_folder_path)
    elif option_number == 4:
        write_list_to_csv_column('Trans X', option_4.option_4(FILE_NAMES), folder_path=CSV_folder_path)
    elif option_number == 5:
        write_list_to_csv_column('trans r', option_5.option_5(FILE_NAMES), folder_path=CSV_folder_path)
    elif option_number == 6:
        write_list_to_csv_column('trans boob', option_6.option_6(FILE_NAMES), folder_path=CSV_folder_path)
    elif option_number == 7:
        option_7.option_7(FILE_NAMES, csv_folder_path=CSV_folder_path)
    elif option_number == 8:
        option_8.option_8(FILE_NAMES, csv_folder_path=CSV_folder_path)
    elif option_number == 9:
        option_9.option_9(FILE_NAMES, csv_folder_path=CSV_folder_path)
    elif option_number == 10:
        option_10.option_10(FILE_NAMES, csv_folder_path=CSV_folder_path)
    elif option_number == 11:
        option_11.option_11(FILE_NAMES, csv_folder_path=CSV_folder_path)
    else:
        raise Exception("Didn't match any options!")

if __name__ == '__main__':
    # source = input('Enter path :')
    source = r'/home/fatguy/Desktop/codes/fiver/image_to_csv/images'
    option_number = input('Enter option :')
    # CSV_folder_path = input('Enter the path of csv folder(to store CSVs) :')
    # CSV_folder_path = fr'{CSV_folder_path}'
    # print(CSV_folder_path)
    CSV_folder_path = r'/home/fatguy/Desktop/codes/fiver/image_to_csv/CSVs'


    main(source, int(option_number), CSV_folder_path)
