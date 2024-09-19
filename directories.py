import json
from contacts import Contact


class Directory():
    def __init__(self):
        self.data = {}
        self.menu = {}
        main_menu = [
            'показать все контакты',
            'создать контакт',
            'найти контакт',
            'выход',
        ]
        for i, item in enumerate(main_menu):
            self.menu[i+1] = item

    def add_contact(self, contact):
        '''Прибавляем id и контакт в справочник'''
        length = len(self.data)+1
        self.data[length] = contact

    def import_data(self, data):
        '''Преобразуем данные в контакт и добавляем в справочник'''
        for key, value in data.items():
            contact = Contact(
                value["name"], value["phone"], value["description"])
            self.add_contact(contact)
        return self.data

    def change_contact(self, id, new_contact):
        '''Изменяем контакт по id'''
        self.data[id] = new_contact

    def remove_contact(self, id):
        '''Удаление контакта по id'''
        del self.data[id]

    def export_data(self):
        '''Преобразуем справочник в словарь'''
        contacts_dict = {}
        for key, contact in self.data.items():
            contacts_dict[str(key)] = contact.to_dict()

        return contacts_dict
