def nok(a, b):
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a + b)


x = int(input('Введите число а ='))
y = int(input('Введите число b='))
print('НОК:', nok(x, y))
