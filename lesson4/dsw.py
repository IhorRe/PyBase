lst = []
dct = {}


def make_list(minumum, maximum, qty):
    from random import random
    for i in range(qty):
        lst.append(int(random() * (maximum - minumum + 1)) + minumum)


def analysis():
    for i in lst:
        if i in dct:
            dct[i] += 1
        else:
            dct[i] = 1


mn = int(input('Минимум: '))
mx = int(input('Максимум: '))
qty = int(input('Количество элементов: '))
make_list(mn, mx, qty)
analysis()
for i in sorted(dct):
    print("'%d':%d" % (i, dct[i])