def area(figure, data):
    if figure == 'круг':
        s = 3.14 * (data[0] ** 2)
    if figure == 'прямоугольник':
        a, b = data
        s = a * b
    if figure == 'треугольник':
        a, b, c = data
        s = (a * b * c) / 2
    return ' Площадь {} = {} '.format(figure, s)


figure = input('Фигура желаемая для расчёта площади =  ')
data = [float(i) for i in input('Введите данные для расчёта пробел = ').rsplit()]
print(area(figure, data))
