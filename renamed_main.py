"""
This is the main module of the project.
"""

import os
import sys
import csv

CSV_FIRST_ROW = ["product_name", "sku", "price", "Sale_price", "photo", "vid", "name", "name-link"]
files_names = []

def get_all_file_names(source_path):
    for root, dirs, files in os.walk(source_path):
        for name in files:
            files_names.append(name)
            files_names.sort()

def retrun_list_elements_as_list(given_list):
    for element in given_list:
        element = list(element)

def write_list_to_csv_column():
    with open('test.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(CSV_FIRST_ROW)

        for val in files_names:
            writer.writerow([val])
        f.close()

def join_name_and_rest_list(name_list, option_list):
    return_list = []
    for i in range(name_list):
        name = name_list[i]
        element = (list(name)).append(option_list)
        return_list.append(element)

    return return_list

def main(source):
    cwd = os.getcwd()
    source_path = os.path.join(cwd, source)

    get_all_file_names(source_path)
    write_list_to_csv_column()


if __name__ == '__main__':
    args = sys.argv
    if len(args) != 2:
        raise Exception("Only pass the folder name.")
    
    source = args[1:]
    source = source[0]
    
    main(source)
