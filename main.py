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
    option_11,
    option_12,
    option_13,
    option_14,
    option_15,
    option_16,
    option_17,
    option_18,
    option_19,
    option_20,
    option_21,
    option_22,
    option_23,
    option_24,
    option_25,
    option_26,
    option_27,
    option_28,
    option_29,
    option_30)


NUMBER_OF_ELEMENTS_PER_OPTION = [4]
# CSV_FIRST_ROW = ["product_name", "sku", "price", "Sale_price", "photo", "video", "name", "name-link"]
FILE_NAMES = []
PHOTO = "{}.jpg|{}_{}_Proof.jpg"
VIDEO = '{}_{}_'


def _date():    # to get today's date
    today = date.today()
    d1 = today.strftime("%d%m20%y")
    return d1


def get_all_file_names(source_path):
    for root, dirs, files in os.walk(source_path):
        for name in files:
            # To get file names without extension
            FILE_NAMES.append(os.path.splitext(name)[0])
            FILE_NAMES.sort()


def write_list_to_3rd_csv(name_of_file, files, folder_path):
    pd.DataFrame(list(zip(*[files[0],
                            files[1]]))).to_csv(os.path.join(folder_path, (name_of_file + '.csv')), index=False, header=False)

    print("3rd csv written...")


def write_list_to_2nd_csv_column(name_of_file, files, folder_path):
    pd.DataFrame(list(zip(*[files[0],
                            files[1],
                            files[2],
                            files[3],
                            files[4],
                            files[5],
                            files[6],
                            files[7]]))).to_csv(os.path.join(folder_path, (name_of_file + '.csv')), index=False, header=False)
    print("2nd csv written...")


def write_list_to_csv_column(name_of_file, files, folder_path):
    df = pd.DataFrame({'product_name': files[0],
                       'sku': files[1],
                       'price': files[2],
                       'Sale_price': files[3],
                       'photos': files[4],
                       'video': files[5],
                       'name': files[6],
                       'name-link': files[7]})
    df.to_csv(os.path.join(folder_path, (name_of_file + '.csv')), index=False)
    print("csv written...")


def option_1(FILE_NAMES):
    product_list = []
    sku_list = []
    price = []
    Sale_price = []
    photo_list = []
    video_list = []
    name_list = []
    name_link = []

    product_name = "{} {} signed XXX 8x10 Photo -PROOF- -CERTIFICATE- (A{})"
    date1 = _date()

    for i in FILE_NAMES:
        file_ele = i.split('_')
        First_name = file_ele[0].title()    # This extracts the first element
        Last_name = file_ele[1].title()     # This extracts the last element
        Last_4 = file_ele[-1]

        # product list
        product_list.append(product_name.format(First_name, Last_name, Last_4))

        # sku list
        sku = First_name + Last_name[0] + f"{Last_4}" + date1 + "X"
        sku_list.append(sku)

        # price
        price.append(29.95)

        # sale price
        Sale_price.append(22.95)

        # photo list
        photo_list.append(PHOTO.format(i, First_name, Last_name))

        # video list
        video_list.append('[video width="360" height="640" mp4="https://stalicali.com/wp-content/uploads/wpallimport/files/' +
                          VIDEO.format(First_name, Last_name) + 'Signing_Autographs_Video.mp4"][/video]')

        # name list
        name_list.append((First_name+" "+Last_name))

        # namelink list
        name_link.append((First_name+"-"+Last_name))

    return [product_list, sku_list, price, Sale_price, photo_list, video_list, name_list, name_link]


def main(source, option_number, CSV_folder_path):
    cwd = os.getcwd()
    source_path = os.path.join(cwd, source)
    get_all_file_names(source_path)

    # check the option number and run the function accordingly
    if option_number == 1:
        write_list_to_csv_column('xxx', option_1(
            FILE_NAMES), folder_path=CSV_folder_path)
    elif option_number == 2:
        inventory_csv_path = input("Enter the inventory sheet path : ")
        # inventory_csv_path = "/home/fatguy/Desktop/codes/fiver/image_to_csv/inventory-1.csv"
        write_list_to_csv_column('reg Boob', option_2.option_2(FILE_NAMES, inventory_csv_path=inventory_csv_path), folder_path=CSV_folder_path)
        write_list_to_2nd_csv_column(
            '2nd-option-2nd', option_2.option_2_2nd_csv(FILE_NAMES), folder_path=CSV_folder_path)
        write_list_to_3rd_csv(
            '2nd-option-3rd', option_2.option_2_3rd_csv(FILE_NAMES), folder_path=CSV_folder_path)
    elif option_number == 3:
        inventory_csv_path = input("Enter the inventory sheet path : ")
        # inventory_csv_path = "/home/fatguy/Desktop/codes/fiver/image_to_csv/inventory-1.csv"
        write_list_to_csv_column('REG', option_3.option_3(
            FILE_NAMES), folder_path=CSV_folder_path)
        write_list_to_2nd_csv_column(
            '3rd-option-2nd', option_3.option_3_2nd_csv(FILE_NAMES, inventory_csv_path), folder_path=CSV_folder_path)
        write_list_to_3rd_csv(
            '3rd-option-3rd', option_3.option_3_3rd_csv(FILE_NAMES), folder_path=CSV_folder_path)
    elif option_number == 4:
        write_list_to_csv_column('Trans X', option_4.option_4(
            FILE_NAMES), folder_path=CSV_folder_path)
    elif option_number == 5:
        inventory_csv_path = input("Enter the inventory sheet path : ")
        # inventory_csv_path = "/home/fatguy/Desktop/codes/fiver/image_to_csv/inventory-1.csv"
        write_list_to_csv_column('trans r', option_5.option_5(
            FILE_NAMES), folder_path=CSV_folder_path)
        write_list_to_2nd_csv_column(
            '5th-option-2nd', option_5.option_5_2nd_csv(FILE_NAMES, inventory_csv_path), folder_path=CSV_folder_path)
        write_list_to_3rd_csv(
            '5th-option-3rd', option_5.option_5_3rd_csv(FILE_NAMES), folder_path=CSV_folder_path)
    elif option_number == 6:
        inventory_csv_path = input("Enter the inventory sheet path : ")
        # inventory_csv_path = "/home/fatguy/Desktop/codes/fiver/image_to_csv/inventory-1.csv"
        write_list_to_csv_column('trans boob', option_6.option_6(FILE_NAMES), folder_path=CSV_folder_path)
        write_list_to_2nd_csv_column('6th-option-2nd', option_6.option_6_2nd_csv(FILE_NAMES, inventory_csv_path), folder_path=CSV_folder_path)
        write_list_to_3rd_csv('6th-option-3rd', option_6.option_6_3rd_csv(FILE_NAMES), folder_path=CSV_folder_path)
    elif option_number == 7:
        inventory_csv_path = input("Enter the inventory sheet path : ")
        # inventory_csv_path = "/home/fatguy/Desktop/codes/fiver/image_to_csv/inventory-1.csv"
        option_7.option_7(FILE_NAMES, csv_folder_path=CSV_folder_path)
        write_list_to_2nd_csv_column('7th-option-2nd', option_7.option_7_2nd_csv(FILE_NAMES, inventory_csv_path=inventory_csv_path), folder_path=CSV_folder_path)
        write_list_to_3rd_csv('7th-option-3rd', option_7.option_7_3rd_csv(FILE_NAMES), folder_path=CSV_folder_path)
    elif option_number == 8:
        inventory_csv_path = input("Enter the inventory sheet path : ")
        # inventory_csv_path = "/home/fatguy/Desktop/codes/fiver/image_to_csv/inventory-1.csv"
        option_8.option_8(FILE_NAMES, csv_folder_path=CSV_folder_path)
        write_list_to_2nd_csv_column('8th-option-2nd', option_8.option_8_2nd_csv(FILE_NAMES, inventory_csv_path=inventory_csv_path), folder_path=CSV_folder_path)
        write_list_to_3rd_csv('8th-option-3rd', option_8.option_8_3rd_csv(FILE_NAMES), folder_path=CSV_folder_path)
    elif option_number == 9:
        option_9.option_9(FILE_NAMES, csv_folder_path=CSV_folder_path)
    elif option_number == 10:
        inventory_csv_path = input("Enter the inventory sheet path : ")
        # inventory_csv_path = "/home/fatguy/Desktop/codes/fiver/image_to_csv/inventory-1.csv"
        option_10.option_10(FILE_NAMES, csv_folder_path=CSV_folder_path)
        write_list_to_2nd_csv_column('10th-option-2nd', option_10.option_10_2nd_csv(FILE_NAMES, inventory_csv_path=inventory_csv_path), folder_path=CSV_folder_path)
        write_list_to_3rd_csv('10th-option-3rd', option_10.option_10_3rd_csv(FILE_NAMES), folder_path=CSV_folder_path)
    elif option_number == 11:
        inventory_csv_path = input("Enter the inventory sheet path : ")
        # inventory_csv_path = "/home/fatguy/Desktop/codes/fiver/image_to_csv/inventory-1.csv"
        option_11.option_11(FILE_NAMES, csv_folder_path=CSV_folder_path)
        write_list_to_2nd_csv_column(
            '11th-option-2nd', option_11.option_11_2nd_csv(FILE_NAMES, inventory_csv_path), folder_path=CSV_folder_path)
        write_list_to_3rd_csv(
            '11th-option-3rd', option_11.option_11_3rd_csv(FILE_NAMES), folder_path=CSV_folder_path)
    elif option_number == 12:
        option_12.option_12(FILE_NAMES, csv_folder_path=CSV_folder_path)
    elif option_number == 13:
        inventory_csv_path = input("Enter the inventory sheet path : ")
        # inventory_csv_path = "/home/fatguy/Desktop/codes/fiver/image_to_csv/inventory-1.csv"
        option_13.option_13(FILE_NAMES, csv_folder_path=CSV_folder_path)
        write_list_to_2nd_csv_column(
            '13th-option-2nd', option_13.option_13_2nd_csv(FILE_NAMES, inventory_csv_path), folder_path=CSV_folder_path)
        write_list_to_3rd_csv(
            '13th-option-3rd', option_13.option_13_3rd_csv(FILE_NAMES), folder_path=CSV_folder_path)
    elif option_number == 14:
        inventory_csv_path = input("Enter the inventory sheet path : ")
        # inventory_csv_path = "/home/fatguy/Desktop/codes/fiver/image_to_csv/inventory-1.csv"
        option_14.option_14(FILE_NAMES, csv_folder_path=CSV_folder_path)
        write_list_to_2nd_csv_column(
            '14th-option-2nd', option_14.option_14_2nd_csv(FILE_NAMES, inventory_csv_path), folder_path=CSV_folder_path)
        write_list_to_3rd_csv(
            '14th-option-3rd', option_14.option_14_3rd_csv(FILE_NAMES), folder_path=CSV_folder_path)
    elif option_number == 15:
        option_15.option_15(FILE_NAMES, csv_folder_path=CSV_folder_path)
    elif option_number == 16:
        inventory_csv_path = input("Enter the inventory sheet path : ")
        # inventory_csv_path = "/home/fatguy/Desktop/codes/fiver/image_to_csv/inventory-1.csv"
        option_16.option_16(FILE_NAMES, csv_folder_path=CSV_folder_path)
        write_list_to_2nd_csv_column(
            '16th-option-2nd', option_16.option_16_2nd_csv(FILE_NAMES, inventory_csv_path), folder_path=CSV_folder_path)
        write_list_to_3rd_csv(
            '16th-option-3rd', option_16.option_16_3rd_csv(FILE_NAMES), folder_path=CSV_folder_path)
    elif option_number == 17:
        inventory_csv_path = input("Enter the inventory sheet path : ")
        # inventory_csv_path = "/home/fatguy/Desktop/codes/fiver/image_to_csv/inventory-1.csv"
        option_17.option_17(FILE_NAMES, csv_folder_path=CSV_folder_path)
        write_list_to_2nd_csv_column(
            '17th-option-2nd', option_17.option_17_2nd_csv(FILE_NAMES, inventory_csv_path), folder_path=CSV_folder_path)
    elif option_number == 18:
        option_18.option_18(FILE_NAMES, csv_folder_path=CSV_folder_path)
    elif option_number == 19:
        write_list_to_csv_column('gay xxx', option_19.option_19(
            FILE_NAMES), folder_path=CSV_folder_path)
    elif option_number == 20:
        inventory_csv_path = input("Enter the inventory sheet path : ")
        # inventory_csv_path = "/home/fatguy/Desktop/codes/fiver/image_to_csv/inventory-1.csv"
        write_list_to_csv_column('Gay Boob', option_20.option_20(
            FILE_NAMES), folder_path=CSV_folder_path)
        write_list_to_2nd_csv_column(
            '20th-option-2nd', option_20.option_20_2nd_csv(FILE_NAMES, inventory_csv_path), folder_path=CSV_folder_path)
        write_list_to_3rd_csv(
            '20th-option-3rd', option_20.option_20_3rd_csv(FILE_NAMES), folder_path=CSV_folder_path)
    elif option_number == 21:
        inventory_csv_path = input("Enter the inventory sheet path : ")
        # inventory_csv_path = "/home/fatguy/Desktop/codes/fiver/image_to_csv/inventory-1.csv"
        write_list_to_csv_column('gay REG', option_21.option_21(
            FILE_NAMES), folder_path=CSV_folder_path)
        write_list_to_2nd_csv_column(
            '21th-option-2nd', option_21.option_21_2nd_csv(FILE_NAMES, inventory_csv_path), folder_path=CSV_folder_path)
        write_list_to_3rd_csv(
            '21th-option-3rd', option_21.option_21_3rd_csv(FILE_NAMES), folder_path=CSV_folder_path)
    elif option_number == 22:
        write_list_to_csv_column('playboy xxx', option_22.option_22(
            FILE_NAMES), folder_path=CSV_folder_path)
    elif option_number == 23:
        write_list_to_csv_column('playboy Boob', option_23.option_23(
            FILE_NAMES), folder_path=CSV_folder_path)
        write_list_to_2nd_csv_column(
            '23rd-option-2nd', option_23.option_23_2nd_csv(FILE_NAMES), folder_path=CSV_folder_path)
        write_list_to_3rd_csv(
            '23rd-option-3rd', option_23.option_23_3rd_csv(FILE_NAMES), folder_path=CSV_folder_path)
    elif option_number == 24:
        inventory_csv_path = input("Enter the inventory sheet path : ")
        # inventory_csv_path = "/home/fatguy/Desktop/codes/fiver/image_to_csv/inventory-1.csv"
        write_list_to_csv_column('playboy REG', option_24.option_24(FILE_NAMES), folder_path=CSV_folder_path)
        write_list_to_2nd_csv_column('24th-option-2nd', option_24.option_24_2nd_csv(FILE_NAMES, inventory_csv_path), folder_path=CSV_folder_path)
        write_list_to_3rd_csv('24th-option-3rd', option_24.option_24_3rd_csv(FILE_NAMES), folder_path=CSV_folder_path)
    elif option_number==25:
        inventory_csv_path = input("Enter the inventory sheet path : ")
        # inventory_csv_path = "/home/fatguy/Desktop/codes/fiver/image_to_csv/rp-inventory.csv"
        option_25.option_25(FILE_NAMES=FILE_NAMES, csv_folder_path=CSV_folder_path, inventory_csv_path=inventory_csv_path)
        write_list_to_3rd_csv('25th-option-3rd', option_25.option_25_3rd_csv(FILE_NAMES), folder_path=CSV_folder_path)
    elif option_number==26:
        inventory_csv_path = input("Enter the inventory sheet path : ")
        # inventory_csv_path = "/home/fatguy/Desktop/codes/fiver/image_to_csv/inventory-1.csv"
        option_26.option_26(FILE_NAMES=FILE_NAMES, csv_folder_path=CSV_folder_path, inventory_csv_path=inventory_csv_path)
        write_list_to_3rd_csv('26th-option-3rd', option_26.option_26_3rd_csv(FILE_NAMES), folder_path=CSV_folder_path)
    elif option_number==27:
        inventory_csv_path = input("Enter the inventory sheet path : ")
        # inventory_csv_path = "/home/fatguy/Desktop/codes/fiver/image_to_csv/inventory-1.csv"
        option_27.option_27(FILE_NAMES=FILE_NAMES, csv_folder_path=CSV_folder_path, inventory_csv_path=inventory_csv_path)
        write_list_to_3rd_csv('27th-option-3rd', option_27.option_27_3rd_csv(FILE_NAMES), folder_path=CSV_folder_path)
    elif option_number==28:
        inventory_csv_path = input("Enter the inventory sheet path : ")
        # inventory_csv_path = "/home/fatguy/Desktop/codes/fiver/image_to_csv/invent.csv"
        option_28.option_28(FILE_NAMES=FILE_NAMES, csv_folder_path=CSV_folder_path, inventory_csv_path=inventory_csv_path)
        write_list_to_3rd_csv('28th-option-3rd', option_28.option_28_3rd_csv(FILE_NAMES), folder_path=CSV_folder_path)
    elif option_number==29:
        inventory_csv_path = input("Enter the inventory sheet path : ")
        # inventory_csv_path = "/home/fatguy/Desktop/codes/fiver/image_to_csv/inventory-1.csv"
        option_29.option_29(FILE_NAMES=FILE_NAMES, csv_folder_path=CSV_folder_path, inventory_csv_path=inventory_csv_path)
        write_list_to_3rd_csv('29th-option-3rd', option_29.option_29_3rd_csv(FILE_NAMES), folder_path=CSV_folder_path)
    elif option_number==30:
        inventory_csv_path = input("Enter the inventory sheet path : ")
        # inventory_csv_path = "/home/fatguy/Desktop/codes/fiver/image_to_csv/inventory-1.csv"
        option_30.option_30(FILE_NAMES=FILE_NAMES, csv_folder_path=CSV_folder_path, inventory_csv_path=inventory_csv_path)
        write_list_to_3rd_csv('30th-option-3rd', option_30.option_30_3rd_csv(FILE_NAMES), folder_path=CSV_folder_path)
    else:
        raise Exception("Didn't match any options!")


if __name__ == '__main__':
    source = input('Enter path :')
    # source = r'/home/fatguy/Desktop/codes/fiver/image_to_csv/temp'
    option_number = input('Enter option :')
    CSV_folder_path = input('Enter the path of csv folder(to store CSVs) :')
    # CSV_folder_path = fr'{CSV_folder_path}'
    # print(CSV_folder_path)
    # CSV_folder_path = r'/home/fatguy/Desktop/codes/fiver/image_to_csv/CSVs'


    main(source, int(option_number), CSV_folder_path)
