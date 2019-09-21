from math import sqrt
print("Привет,")
print("Давай посчитаем площадь треугольника")
a = float(input("введи сторону а треугольника ="))
b = float(input("введи сторону b треугольника ="))
c = float(input("введи сторону с треугольника ="))
p = sum((a, b, c)) / 2
s = sqrt((p * (p - a) * (p - b) * (p - c)))
print("Площадь треугольника = ", s)