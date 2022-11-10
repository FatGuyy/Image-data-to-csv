"""
This is the main module of the project.
"""

import os
import sys
import csv
import some

CSV_FIRST_ROW = ["product_name", "sku", "price", "Sale_price", "photo", "vid", "name", "name-link"]
FILE_NAMES = []

def get_all_file_names(source_path):
    temp_list_for_names =[]
    for root, dirs, files in os.walk(source_path):
        for name in files:
            temp_list_for_names.append(name)
        temp_list_for_names.sort()
    return temp_list_for_names

# def retrun_list_elements_as_list(given_list):
    # for element in given_list:
        # element = list(element)


def write_list_to_csv_column():
    with open('test.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(CSV_FIRST_ROW)

        for val in FILE_NAMES:
            writer.writerow([val])
        f.close()

def write_list_to_csv_row(row_list):
    pass

def join_name_and_rest_list(name_list, option_list):
    for i in range(0, len(name_list)):
        name = name_list[i]
        print(name)
        option_list[i].insert(0, name)    

    return option_list

def main(source):
    source_path = fr'{source}'

    FILE_NAMES = get_all_file_names(source_path)
    # write_list_to_csv_column()
    option_1_data = some.option_1()
    print(join_name_and_rest_list(FILE_NAMES, option_1_data))

if __name__ == '__main__':
    args = sys.argv
    if len(args) != 2:
        raise Exception("Only pass the folder name.")
    
    source = args[1:]
    source = source[0]
    
    main(source)
