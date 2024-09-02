import json
PATH = 'Directory.json'


def Open_File(file_Name=PATH):
    '''Читаем и запоминаем файл'''
    with open(file_Name, 'a+', encoding='UTF-8') as file:
        file.seek(0)
        data = file.read()
        if data:
            return json.loads(data)
        else:
            return {}


def Save_File(data: str, file_Name: str):
    '''Сохраняем файл'''
    with open(file_Name, 'w+', encoding='UTF-8') as file:
        file.seek(0)
        json.dump(data, file, indent=4, ensure_ascii=False)
        return


def Show_Contacts(data: str):
    '''выбираем нужные атрибуты и выводим'''
    print(f"{'Phone':<15}{'Name':<10}{'Description':<20}")
    for key, value in data.items():
        show_data = {
            "name": value['name'],
            "phone": value['phone'],
            "description": value['description']
        }
        print(f"{show_data["phone"]:<15}{show_data["name"]:<10}{
              show_data["description"]:<20}")


def Create_Contact(data: str):
    '''Добавляем новое значение'''
    new_record = {
        "name": input('Введите имя: '),
        "phone": input('Введите номер: '),
        "description": input('Введите описание: ')
    }
    new_key = str(max(map(int, data.keys()), default=0) + 1)
    data[new_key] = new_record
    return data


def Find_Contact(data: str):
    '''
    Поиск записи
    Сначала поиск всех совпадений и добавление в пустой словарь
    После чего вывод поочередно найденные записи
    '''
    found_Dict = {}
    find_Value = input('Введите значение поиска: ')
    for key, value in data.items():
        if find_Value in value['name'] or find_Value in value['phone'] or find_Value in value['description']:
            show_data = {
                "name": value['name'],
                "phone": value['phone'],
                "description": value['description']
            }
            found_Dict[key] = value
    print("\n"*20)
    print(f'Найдено {len(found_Dict.keys())} записей:')
    for i, (key, value) in enumerate(found_Dict.items()):
        print("\n")
        print(
            f"{i+1} запись:\t{value["phone"]:<15}{value["name"]:<10}{value["description"]:<20}\n")
        show_item_Menu(data, key, value)


def Change_Contact(data: str, key: int, value: str):
    '''Изменение записи'''
    for value_name, value in data[key].items():
        print("\n"*20)
        new_Value = input(f"{value_name} = {
                          value}\nВведите новое значение если хотите изменить :")
        if new_Value:
            data[key][value_name] = new_Value
    print("-"*35)


def Remove_Contact(data: str, key: int, value: str):
    '''Удаление записи'''
    print("\n"*20)
    print(f"{value["phone"]:<15}{value["name"]:<10}{value["description"]:<20}")
    approve = input('Действительно хотите удалить запсиь? Default(n) Y/n')
    if approve.lower() == 'y':
        data.pop(key)


def Exit_Directory(data: str, file_Name=PATH):
    '''выход из программы'''
    print('\n'*20)
    is_Save = input('Срхранить файл? default(Y) Y/n: ')
    if is_Save.lower() != 'n':
        Save_File(data, file_Name) if file_Name else Save_File(data)
    else:
        return


def show_main_Menu(data: str, name=None):
    '''ПОказать главное меню'''
    main_Menu = [
        'показать все контакты',
        'создать контакт',
        'найти контакт',
        'выход',
    ]
    dict_Main_Menu = {}
    for i, item in enumerate(main_Menu):
        dict_Main_Menu[i+1] = item
        print(f'{i+1}: {item}')
    if name:
        name = name.lower()
        if name == 'показать все контакты':
            print('\n'*20)
            Show_Contacts(data)
        elif name == 'создать контакт':
            print('\n'*20)
            Create_Contact(data)
        elif name == 'найти контакт':
            print('\n'*20)
            Find_Contact(data)
        elif name == 'выход':
            print('\n'*20)
            Exit_Directory(data)
    return dict_Main_Menu


def show_item_Menu(data: str, key: int, value: str):
    '''Показать подменю'''
    item_Menu = [
        'изменить контакт',
        'удалить контакт',
        'выход'
    ]
    dict_Item_Menu = {}
    for i, item in enumerate(item_Menu):
        dict_Item_Menu[i+1] = item
        print(f'{i+1}: {item}')
    print("-"*20)

    chosen = input("Выберите пункт меню (Если не та запись, нажмите Enter)")

    if chosen and chosen.isdigit():
        if int(chosen) in dict_Item_Menu.keys() and dict_Item_Menu[int(chosen)] != 'выход':
            if dict_Item_Menu[int(chosen)] == 'изменить контакт':
                Change_Contact(data, key, value)
            elif dict_Item_Menu[int(chosen)] == 'удалить контакт':
                Remove_Contact(data, key, value)
        elif dict_Item_Menu[int(chosen)] == 'выход':
            show_main_Menu(data)
        else:
            return
    else:
        print('Некорректный ввод')


# Открываем и считываем справочник
file_Name = input(f'Введите имя файла(по умолчанию {PATH}): ')
data = Open_File(file_Name) if file_Name else Open_File()

work_Flag=True
print("-"*20)
while work_Flag:

    dict_Main_Menu = show_main_Menu(data)
    print("-"*20)

    # Читаем выбор пользователя
    chosen = input("Выберите пункт меню ")

    if chosen and chosen.isdigit():
        # Если выбор корректный и не "выход"
        if int(chosen) in dict_Main_Menu.keys() and dict_Main_Menu[int(chosen)] != 'выход':
            # Показываем меню
            show_main_Menu(data, dict_Main_Menu[int(chosen)])
            print("-"*20)
        # Если выход
        elif dict_Main_Menu[int(chosen)] == 'выход':
            Exit_Directory(
                data, file_Name) if file_Name else Exit_Directory(data)
            work_Flag = False
        else:
            print('Некорректный ввод')
    else:
        print('Некорректный ввод')
