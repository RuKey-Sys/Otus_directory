from directory import PATH
from contacts import Contact

def input_file_name(PATH=PATH):
    file_name = input(f'Введите имя файла(по умолчанию {PATH}): ')
    return file_name


def choose_item_menu():
    return input("Выберите пункт меню ")


def incorrect_input():
    return print('Некорректный ввод')


def enter_value():
    return input("Введите значение поиска: ")

def choose_second_item():
    return input("Выберите пункт меню (Если не та запись, нажмите Enter)")


def show_main_menu(menu: dict):
    '''Показать главное меню'''
    for key,value in menu.items():
        print(f'{key}: {value}')
    return

def show_item_Menu():
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
    return dict_Item_Menu


def create_contact():
    '''Добавляем новое значение'''
    new_record = {
        "name": input('Введите имя: '),
        "phone": input('Введите номер: '),
        "description": input('Введите описание: ')
    }
    return new_record

def show_contact(i,k,value):
    print(f'запись: {i+1}/{k}')
    print("\n")
    print(
        f"{value["phone"]:<15}{value["name"]:<10}{value["description"]:<20}\n")
    
def show_contacts(data: dict):
    '''выбираем нужные атрибуты и выводим'''
    print(f"{'Phone':<15}{'Name':<10}{'Description':<20}")
    for item in data.data.values():
        print(Contact.show_contact(item))