# from option 25
def col_f(colData, _sku, names, max, inventory_csv_path):
    with open(inventory_csv_path, "r") as file:
        data = list(csv.reader(file))
    data1 = data[0]
    app_list = []
    ret = []
    col_I = colData[data1[8]].tolist()
    col_H = colData[data1[7]].tolist()
    
    # gets all unique elemnts of list
    for _ in range(len(col_I)):
        app_list.append('')
    names = reduce(lambda re, x: re+[x] if x not in re else re, names, [])
    
    for name in names:
        sku_index = []
        name_index = []
        for idx, value in enumerate(col_I):
            if value.lower() == _sku.lower():
                sku_index.append(idx)
        for idx, value in enumerate(col_H):
            if(value.lower() == name.lower()):
                name_index.append(idx)
        # print("names F : ",name_index)

        match = list(set(sku_index).intersection(name_index))
        match.sort()
        # print("match - ", match)

        # sorts the start and end of data - of all matches.
        c = count()
        result = [list(g) for _, g in groupby(match, key=lambda x: x-next(c))]
        for i in result:
            ret.append([i[0],i[-1]])


        for i in ret:
            for j in i:
                app_list[j] = 24

    return(app_list[:max])