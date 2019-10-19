import pickle

fn = 'Adress_book.txt'


class members:
    el = {}  # nl - number list

    try:
        f = open(fn, 'rb')
        el = pickle.load(f)
        f.close()
    except:
        pass

    def addmember(self):  # name - имя человека, pn - номер его телефона
        '''Служит для добавления в лист человека и его номера'''
        name = input('Введите имя контакта : ')
        pn = input('Введите номер e-mail адрес : ')  # номер телефона

        if not name in members.el:
            members.el[name] = pn
            print("контакт с адресом " + members.el[name] + " успешно добавлен")

        else:
            print("Контакт с таким именем уже существует")

    def delmember(self):
        delstat = True
        while delstat == True:
            name = input('Введите имя контакта, который вы хотите удалить : ')
            if name in members.el:

                del members.el[name]
                print('Контакт успешно удален')
                delstat = False

            else:
                print('Такого контакта не существует')
                name = input('Введите имя заново : ')

    def editmember(self):
        sstat = True
        s = input('Что вы хотите изменить?(имя или адрес?) : ')
        while sstat == True:
            if s.lower() == 'адрес':
                name = input('Введите имя человека, e-mail адрес которого вы хотите изменить : ')
                if name in members.el:
                    ps = {}
                    ps[name] = input('Введите новый e-mail : ')
                    del members.el[name]
                    members.el[name] = ps[name]
                    del ps[name]
                    print('Номер e-mail успешно изменен')
                    sstat = False
                else:
                    print('Такой контакт не найден')

            elif s.lower() == 'имя':
                name = input('Введите имя человека, которое вы хотите изменить : ')
                if name in members.el:
                    ps = {}
                    ps[name] = input('Введите новое имя контакта : ')
                    del members.el[name]
                    members.el[name] = ps[name]
                    del ps[name]
                    print('Имя успешно изменено новый контакт: ' + members.el[name])
                    sstat = False

                else:
                    print('Такой контакт не найден')

            else:
                print('Было введено неверное значение')
                input('Введите запрос заново')

    def showmember(self):
        print(members.el)

    def showusermember(self):
        usermemberstat = True
        name = input('Введите имя контакта, номер которого вы хотите увидеть : ')
        while usermemberstat == True:
            if name in members.el:
                print('E-mail контакта ' + name + ' :' + members.el[name])
                usermemberstat = False
            else:
                print('Такой e-mail не найден')
                name = input('Введите имя заново : ')

m = members()  # Тот же самый класс, для более легкого доступа
# md хранит имя, чтобы определить необходимую команду
md = input('Для пояснения возможностей введите help : ')
mdstat = True
while mdstat:
    if md.lower() == 'help':
        print(
                'Чтобы изменить список пишите: "изменить",'
                '\nесли хотите добавить конатакт, пишите "добавить",'
                '\nесли удалить контакт пишите: "удалить",'
                '\nесли вы хотите увидеть список контактов введите: "показать",'
                '\nесли хотите увидеть  e-mail контакта введите: "найти" : ')
        md = input('Что вы хотите сделать со списком? : ')

    elif md.lower() == 'изменить':
        if not len(members.el) == 0:
            m.editmember()

        else:
            print('Но список пуст!')
            md = 'добавить'

    elif md.lower() == 'добавить':
        m.addmember()
        mdstat = False

    elif md.lower() == 'удалить':
        if not len(members.el) == 0:
            m.delmember()
            mdstat = False
        else:
            print('Но список пуст, давайте добавим контакт!')
            md = 'добавить'

    elif md.lower() == 'показать':
        m.showmember()
        mdstat = False

    elif md.lower() == 'найти':
        if not len(members.el) == 0:
            m.showusermember()
            mdstat = False
        else:
            print('Но список пуст, давайте добавим контакт!')
            md = 'добавить'
    else:
        print("Неверный выбор")
f = open(fn, 'wb')
pickle.dump(members.el, f)
f.close()