import json
from directory import PATH
from contacts import Contact


def open_file(file_Name=PATH):
    '''Читаем и запоминаем файл'''
    with open(file_Name, 'a+', encoding='UTF-8') as file:
        file.seek(0)
        data = file.read()
        if data:
            return json.loads(data)
        else:
            return {}


def save_file(data: dict, file_Name: str):
    '''Сохраняем файл'''
    json_string = data.export_data()
    with open(file_Name, 'w+', encoding='UTF-8') as file:
        file.seek(0)
        json.dump(json_string,file,indent=4, ensure_ascii=False)
        return


def find_contact(directory: dict, search_value: str):
    '''
    Поиск записи по имени, номеру или описанию.
    Возвращает словарь с найденными контактами.
    '''
    search_value = search_value.lower()
    found_contacts = {}

    for key, contact in directory.data.items():
        # Приводим поля контакта к нижнему регистру для корректного поиска
        if (search_value in contact.name.lower() or 
            search_value in contact.number or 
            search_value in contact.description.lower()):
            
            # Формируем данные для отображения
            found_contacts[key] = {
                "name": contact.name,
                "phone": contact.number,
                "description": contact.description
            }

    return found_contacts


def change_contact(directory: dict, key: int, contact: dict):
    '''Изменение записи'''
    new_contact ={}
    contact = Contact(contact["name"], contact["phone"], contact["description"])
    new_name = input(f"Имя ({contact.name}): ").strip()
    new_phone = input(f"Телефон ({contact.number}): ").strip()
    new_description = input(f"Описание ({contact.description}): ").strip()

    # Проверяем, введены ли новые значения, иначе оставляем старые
    updated_name = new_name if new_name else contact.name
    updated_phone = new_phone if new_phone else contact.number
    updated_description = new_description if new_description else contact.description
    updated_contact = Contact(updated_name, updated_phone, updated_description)
    directory.change_contact(key, updated_contact)

    return directory

def remove_contact(directory: dict, key: int, contact: dict):
    '''Удаление записи'''
    print("\n"*20)
    print(f"{contact["phone"]:<15}{contact["name"]:<10}{contact["description"]:<20}")
    approve = input('Действительно хотите удалить запсиь? Default(n) Y/n')
    if approve.lower() == 'y':
        directory.remove_contact(key)


def exit_directory(data: str, file_Name=PATH):
    '''выход из программы'''
    print('\n'*20)
    is_Save = input('Срхранить файл? default(Y) Y/n: ')
    if is_Save.lower() != 'n':
        save_file(data, file_Name) if file_Name else save_file(data)
    else:
        return



