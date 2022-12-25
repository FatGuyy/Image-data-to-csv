"""
This file gets the 23th option. (back to one name only)
"""
from datetime import date

FILE_NAMES = []
PHOTO = "{}.jpg|{}_{}_Proof.jpg"
VIDEO =  '{}_{}_'
product_list  = []
sku_list = []

def _date():    # to get today's date
    today = date.today()
    d1 = today.strftime("%d%m20%y")
    return d1

def option_23(FILE_NAMES):
    price = []
    Sale_price = []
    photo_list = []
    video_list = []
    name_list = []
    name_link = []
    product_name = "{} {} signed Playboy model B 8x10 Photo -PROOF- -CERTIFICATE- (A{})"
    date1 = _date()

    for i in FILE_NAMES:
        file_ele = i.split('_')
        First_name = file_ele[0].title()    # This extracts the first element
        Last_name = file_ele[1].title()     # This extracts the last element
        Last_4 = file_ele[-1]

        # product list
        product_list.append(product_name.format(First_name,Last_name,Last_4))
        
        #sku list
        sku = First_name + Last_name[0] + f"{Last_4}" + date1 + "prb"
        sku_list.append(sku)

         # price
        price.append(59.95)

        # sale price
        Sale_price.append(44.95)

        # photo list
        photo_list.append(PHOTO.format(i, First_name, Last_name))
        
        # video list
        video_list.append('[video width="360" height="640" mp4="https://stalicali.com/wp-content/uploads/wpallimport/files/' + VIDEO.format(First_name, Last_name) + 'Signing_Autographs_Video.mp4"][/video]')

        # name list
        name_list.append((First_name+" "+Last_name))

        # namelink list
        name_link.append((First_name+"-"+Last_name))

    return [product_list, sku_list, price, Sale_price, photo_list, video_list, name_list, name_link]

def option_23_2nd_csv(FILE_NAMES):
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
        last_sku.append("prb")

    return [product_list, sku_list, price, column_d, column_e, column_f, column_g, last_sku]

def option_23_3rd_csv(FILE_NAMES):
    column_a = []

    for _ in FILE_NAMES:
        # column a
        column_a.append(1)

    return ([column_a, sku_list])
