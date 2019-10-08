def calc(n):
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return count


n = abs(int(input('Введите целое число = ')))
print('Количество цифр в нём =', calc(n))
