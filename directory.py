import json
PATH = 'Directory'


def OpenFile(fileName=PATH):  # Читаем и запоминаем файл
    with open(fileName, 'a+', encoding='UTF-8') as file:
        file.seek(0)
        data = file.read()
        if data:
            return json.loads(data)
        else:
            return {}


def SaveFile(data, file_Name):  # Сохраняем файл
    with open(file_Name, 'w+', encoding='UTF-8') as file:
        file.seek(0)
        json.dump(data, file, indent=4, ensure_ascii=False)
        return


def ShowContacts(data):  # выбираем нужные атрибуты и выводим
    print(f"{'Phone':<15}{'Name':<10}{'Description':<20}")
    for key, value in data.items():
        show_data = {
            "name": value['name'],
            "phone": value['phone'],
            "description": value['description']
        }
        print(f"{show_data["phone"]:<15}{show_data["name"]:<10}{
              show_data["description"]:<20}")


def CreateContact(data):  # Добавляем новое значение
    new_record = {
        "name": input('Введите имя: '),
        "phone": input('Введите номер: '),
        "description": input('Введите описание: ')
    }
    new_key = str(max(map(int, data.keys()), default=0) + 1)
    data[new_key] = new_record
    return data


def FindContact(data):  # Поиск записи
    found_Dict = {}
    findValue = input('Введите значение поиска: ')
    # Сначала поиск всех совпадений и добавление в пустой словарь
    for key, value in data.items():
        if findValue in value['name'] or findValue in value['phone'] or findValue in value['description']:
            show_data = {
                "name": value['name'],
                "phone": value['phone'],
                "description": value['description']
            }
            found_Dict[key] = value
    print("\n"*20)
    # После чего вывод поочередно найденные записи
    print(f'Найдено {len(found_Dict.keys())} записей:')
    for i, (key, value) in enumerate(found_Dict.items()):
        print("\n")
        print(
            f"{i+1} запись:\t{value["phone"]:<15}{value["name"]:<10}{value["description"]:<20}\n")
        show_itemMenu(data, key, value)


def ChangeContact(data, key, value):  # Изменение записи
    for value_name, value in data[key].items():
        print("\n"*20)
        new_Value = input(f"{value_name} = {
                          value}\nВведите новое значение если хотите изменить :")
        if new_Value:
            data[key][value_name] = new_Value
    print("-"*35)


def RemoveContact(data, key, value):  # Удаление записи
    print("\n"*20)
    print(f"{value["phone"]:<15}{value["name"]:<10}{value["description"]:<20}")
    approve = input('Действительно хотите удалить запсиь? Default(n) Y/n')
    if approve.lower() == 'y':
        data.pop(key)


def ExitDirectory(data, file_Name=PATH):  # выход из программы
    print('\n'*20)
    isSave = input('Срхранить файл? default(Y) Y/n: ')
    if isSave.lower() != 'n':
        SaveFile(data, file_Name) if file_Name else SaveFile(data)
    else:
        return


def show_mainMenu(data, name=None):  # ПОказать главное меню
    mainMenu = [
        'показать все контакты',
        'создать контакт',
        'найти контакт',
        'выход',
    ]
    dict_MainMenu = {}
    for i, item in enumerate(mainMenu):
        dict_MainMenu[i+1] = item
        print(f'{i+1}: {item}')
    if name:
        name = name.lower()
        if name == 'показать все контакты':
            print('\n'*20)
            ShowContacts(data)
        elif name == 'создать контакт':
            print('\n'*20)
            CreateContact(data)
        elif name == 'найти контакт':
            print('\n'*20)
            FindContact(data)
        elif name == 'выход':
            print('\n'*20)
            ExitDirectory(data)
    return dict_MainMenu


def show_itemMenu(data, key, value):  # Показать подменю
    itemMenu = [
        'изменить контакт',
        'удалить контакт',
        'выход'
    ]
    dict_ItemMenu = {}
    for i, item in enumerate(itemMenu):
        dict_ItemMenu[i+1] = item
        print(f'{i+1}: {item}')
    print("-"*20)

    chosen = input("Выберите пункт меню (Если не та запись, нажмите Enter)")

    if chosen and chosen.isdigit():
        if int(chosen) in dict_ItemMenu.keys() and dict_ItemMenu[int(chosen)] != 'выход':
            if dict_ItemMenu[int(chosen)] == 'изменить контакт':
                ChangeContact(data, key, value)
            elif dict_ItemMenu[int(chosen)] == 'удалить контакт':
                RemoveContact(data, key, value)
        elif dict_ItemMenu[int(chosen)] == 'выход':
            show_mainMenu(data)
        else:
            return
    else:
        print('Некорректный ввод')


# Открываем и считываем справочник
file_Name = input(f'Введите имя файла(по умолчанию {PATH}): ')
data = OpenFile(file_Name) if file_Name else OpenFile()


print("-"*20)
while True:

    dict_MainMenu = show_mainMenu(data)
    print("-"*20)

    # Читаем выбор пользователя
    chosen = input("Выберите пункт меню ")

    if chosen and chosen.isdigit():
        # Если выбор корректный и не "выход"
        if int(chosen) in dict_MainMenu.keys() and dict_MainMenu[int(chosen)] != 'выход':
            # Показываем меню
            show_mainMenu(data, dict_MainMenu[int(chosen)])
            print("-"*20)
        # Если выход
        elif dict_MainMenu[int(chosen)] == 'выход':
            ExitDirectory(
                data, file_Name) if file_Name else ExitDirectory(data)
            break
        else:
            print('Некорректный ввод')
    else:
        print('Некорректный ввод')
