'''
missing numbers in sorted list
'''

col_G = [1, 1, 1, 2, 2, 3, 4, 5, 20441, 20441, 20441, 20441, 20441, 20441, 1, 1, 1, 5, 2, 2, 1, 1, 4, 4, 4]
col_G.sort()
b = [x for x in range(col_G[0], col_G[-1] + 1)]
a = set(col_G)

print("missing numbers", list(a ^ set(b)))

# ex = [*set(col_G)]
ex = col_G
otherOne = []
for i in range(0, len(ex)):
    number = next(iter(set(range(min(ex)+1, max(ex))) - set(ex)))
    ex.append(number)
    otherOne.append(number)
print([*set(col_G)])
print(otherOne)
