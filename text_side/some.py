"""
        # number_of_iterations = (len(lines))/7
        # # print(number_of_iterations)
        # # print(lines[:7])
        # while number_of_iterations >=0:
        #     for line in lines[:7]:
        #         # print(line.strip())
        #         LINE_LIST.append(line.strip())
        #     RETURN_LIST.append(LINE_LIST)

        #     number_of_iterations -= 1
        # print(LINE_LIST)
        # print(RETURN_LIST)


write in csv

    # with open(first_csv_name, 'w') as out_file:
        # writer = csv.writer(out_file)
        # writer.writerow(['product_name', 'sku', 'price', 'sale-price', 'photos', 'vid', 'name', 'namelink'])    
        # writer.writerow(Line_list)
"""
import csv

RETURN_LIST = []
LINE_LIST = []
FIRST_CSV_NAME = "test.csv" 

def option_1():
    """
    Iterates 8 times, i.e has 8 elements.
    """
    with open('dummy.txt', 'r+') as fd:
        lines = fd.readlines()
        fd.seek(0)
        fd.writelines(line for line in lines if line.strip())
        fd.truncate()

    with open ('dummy.txt', 'r', encoding='utf-8') as in_file:
        file_data = in_file.read()
        lines = file_data.splitlines()
        chunks = [lines[x:x+7] for x in range(0, len(lines), 7)]
        # print(chunks)
    return chunks

if __name__ == "__main__":
    option_1()
