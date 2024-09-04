import json
PATH = 'Directory.json'


def open_file(file_name=PATH):
    '''Читаем и запоминаем файл'''
    with open(file_name, 'a+', encoding='UTF-8') as file:
        file.seek(0)
        data = file.read()
        if data:
            return json.loads(data)
        else:
            return {}


def save_file(data: str, file_name: str):
    '''Сохраняем файл'''
    with open(file_name, 'w+', encoding='UTF-8') as file:
        file.seek(0)
        json.dump(data, file, indent=4, ensure_ascii=False)
        return


def show_contacts(data: str):
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


def create_contact(data: str):
    '''Добавляем новое значение'''
    new_record = {
        "name": input('Введите имя: '),
        "phone": input('Введите номер: '),
        "description": input('Введите описание: ')
    }
    new_key = str(max(map(int, data.keys()), default=0) + 1)
    data[new_key] = new_record
    return data


def find_contact(data: str):
    '''
    Поиск записи
    Сначала поиск всех совпадений и добавление в пустой словарь
    После чего вывод поочередно найденные записи
    '''
    found_dict = {}
    find_value = input('Введите значение поиска: ')
    for key, value in data.items():
        if find_value in value['name'] or find_value in value['phone'] or find_value in value['description']:
            show_data = {
                "name": value['name'],
                "phone": value['phone'],
                "description": value['description']
            }
            found_dict[key] = value
    print("\n"*20)
    print(f'Найдено {len(found_dict.keys())} записей:')
    for i, (key, value) in enumerate(found_dict.items()):
        print("\n")
        print(
            f"{i+1} запись:\t{value["phone"]:<15}{value["name"]:<10}{value["description"]:<20}\n")
        show_item_menu(data, key, value)


def change_contact(data: str, key: int, value: str):
    '''Изменение записи'''
    for value_name, value in data[key].items():
        print("\n"*20)
        new_value = input(f"{value_name} = {
                          value}\nВведите новое значение если хотите изменить :")
        if new_value:
            data[key][value_name] = new_value
    print("-"*35)


def remove_contact(data: str, key: int, value: str):
    '''Удаление записи'''
    print("\n"*20)
    print(f"{value["phone"]:<15}{value["name"]:<10}{value["description"]:<20}")
    approve = input('Действительно хотите удалить запсиь? Default(n) Y/n')
    if approve.lower() == 'y':
        data.pop(key)


def exit_directory(data: str, file_name=PATH):
    '''выход из программы'''
    print('\n'*20)
    is_save = input('Срхранить файл? default(Y) Y/n: ')
    if is_save.lower() != 'n':
        save_file(data, file_name) if file_name else save_file(data)
    else:
        return


def show_main_menu(data: str, name=None):
    '''Показать главное меню'''
    main_menu = [
        'показать все контакты',
        'создать контакт',
        'найти контакт',
        'выход',
    ]
    dict_main_menu = {}
    for i, item in enumerate(main_menu):
        dict_main_menu[i+1] = item
        print(f'{i+1}: {item}')
    if name:
        name = name.lower()
        if name == 'показать все контакты':
            print('\n'*20)
            show_contacts(data)
        elif name == 'создать контакт':
            print('\n'*20)
            create_contact(data)
        elif name == 'найти контакт':
            print('\n'*20)
            find_contact(data)
        elif name == 'выход':
            print('\n'*20)
            exit_directory(data)
    return dict_main_menu


def show_item_menu(data: str, key: int, value: str):
    '''Показать подменю'''
    item_menu = [
        'изменить контакт',
        'удалить контакт',
        'выход'
    ]
    dict_item_menu = {}
    for i, item in enumerate(item_menu):
        dict_item_menu[i+1] = item
        print(f'{i+1}: {item}')
    print("-"*20)

    chosen = input("Выберите пункт меню (Если не та запись, нажмите Enter)")

    if chosen and chosen.isdigit():
        if int(chosen) in dict_item_menu.keys() and dict_item_menu[int(chosen)] != 'выход':
            if dict_item_menu[int(chosen)] == 'изменить контакт':
                change_contact(data, key, value)
            elif dict_item_menu[int(chosen)] == 'удалить контакт':
                remove_contact(data, key, value)
        elif int(chosen) in dict_item_menu.keys() and dict_item_menu[int(chosen)] == 'выход':
            show_main_menu(data)
        else:
            return
    else:
        print('Некорректный ввод')


# Открываем и считываем справочник
file_name = input(f'Введите имя файла(по умолчанию {PATH}): ')
data = open_file(file_name) if file_name else open_file()

work_flag=True
print("-"*20)
while work_flag:

    dict_main_menu = show_main_menu(data)
    print("-"*20)

    # Читаем выбор пользователя
    chosen = input("Выберите пункт меню ")

    if chosen and chosen.isdigit():
        # Если выбор корректный и не "выход"
        if int(chosen) in dict_main_menu.keys() and dict_main_menu[int(chosen)] != 'выход':
            # Показываем меню
            show_main_menu(data, dict_main_menu[int(chosen)])
            print("-"*20)
        # Если выход
        elif int(chosen) in dict_main_menu.keys() and  dict_main_menu[int(chosen)] == 'выход':
            exit_directory(
                data, file_name) if file_name else exit_directory(data)
            work_flag = False
        else:
            print('Некорректный ввод')
    else:
        print('Некорректный ввод')
