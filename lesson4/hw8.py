print("Привет")
print("Введите текст для редактирования")
a = str(input("текст для экспериментов: "))
print("Вы ввели число =", a.isdigit())
print("Вы ввели текст =", a.isalpha())
txt=a
print(a)
print("Преобразовываем в список")
print(list(a))
syms = len(a) - a.count(' ')
print("В вашем тексте =", syms, "символов")
words = a.count(' ') + 1
print("В Вашем тексте =", words, "слов")
list = [a]
b = int(input("с какого символа начать срез ="))
print(a[b:])
c = int(input("Каким символом закончить срез ="))
print(a[b:-c])
x=txt.upper()
print("Все буквы заглавные")
print(x)
print("Сортировка А-Я", sorted(txt))
y=txt.lower()
print("Все буквы маленькие")
print(y)

