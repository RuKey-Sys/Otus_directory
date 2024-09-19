class Contact():
    def __init__(self, name, number, description):
        '''Инициализируем объект'''
        self.name = name
        self.number = number
        self.description = description

    def show_contact(self):
        '''Возвращаем объект в виде строки'''
        return f"{self.number:<15}{self.name:<10}{self.description:<20}"

    def change_contact(self, value: dict):
        '''Изменяем контакт'''
        self.name = value["name"]
        self.number = value["phone"]
        self.description = value["description"]

    def to_dict(self):
        '''Возвращаем объект в виде словаря'''
        return {
            "name": self.name,
            "phone": self.number,
            "description": self.description
        }

    @staticmethod
    def validate_number(number):
        if len(number) == 10 and number.isdigit():
            return True
        return False
