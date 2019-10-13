def text_stat(text):
    print("статистика символов ----->")
    l = []
    s = ''.join(list(text))
    for i in s:
        if i not in l and i.isalpha() or i.isascii():
            print(i + ': ' + str(s.count(i)))
            l.append(i)
    print("<-----Статистика символов")
    print("*"*50)
    print("статистика слов ---->")
    words1 = text
    words1 = words1.split()
    for i in words1:
        if i not in l and i.isascii() or i.isalpha():
            print(i + ': ' + str(words1.count(i)))
            l.append(i)
    print ('<----- статистика слов')


text = input('текст для экспериментов: ')
print(text_stat(text))