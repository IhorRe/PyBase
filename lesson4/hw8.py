def count1(text):
    count1=0
    while True:
        s = text
        for i in s:
            if i in '0123456789':
                count1 += 1
        return 'В тексте {} цыфр'.format(count1)

def text_stat(text):
    z = text.lower( )
    print("статистика символов ----->")
    l = []
    s = ''.join(list(z))
    for i in s:
        if i not in l and i.isprintable():
            l+=i
            print("'"+i+"'" + ': ' + str(s.count(i)))
    print("<-----Статистика символов")
    print("*"*50)
    print("статистика слов ---->")
    words1 = z
    words1 = words1.split()
    for i in words1:
        if i not in l and i.isascii() or i.isalpha():
            print("'"+i+"'" + ': ' + str(words1.count(i)))
    print('<----- статистика слов')

print('текст для экспериментов:  ')
text = ""
count= 0
stopword = ""
while True:
    line = input( )
    if line.strip() == stopword:
        break
    count+=1
    text += "%s\n" % line
print("<-----------Исходный текс: ")
print(text)
print("Исходный текс-------------> ")
print(count1(text))
print("Количество строк в тексте:  ", count)
print(text_stat(text))