print("Давай поиграем")
n = int(input("введите количество спичек = "))
if n>0:
    while n != 0 and n>0:
        b = int(input("Игорок 1 возьмите спички(не больше 3) = "))
        if b >= 1 and 3 >= b:
            n = n - b
            if n > 0:
                print("Остаток спичек на столе =", n)
            else:
                print("Игрок 1 проиграл")
                break
        else:
            print("неверное количество взятых спичек!!!")
            break
        c = int(input("Игорок 2 возьмите спички(не больше 3) = "))
        if c >= 1 and 3 >= c:
            n = n - c
            if n > 0:
                print("Остаток спичек на столе =", n)
            else:
                print("Игрок 2 проиграл")
                break
        else:
            print("неверное количество взятых спичек!!!")
            break
else:
    print("на столе пусто")
