class Menu:
    def __init__(self, items: dict, title: str = "Меню"):
        """
        Инициализация меню.
        :param items: Словарь с пунктами меню {номер: "название пункта"}.
        :param title: Заголовок меню (по умолчанию "Меню").
        """
        self.items = items
        self.title = title

    def display(self):
        """Отображает меню с заголовком."""
        print(f"==== {self.title} ====")
        for key, value in self.items.items():
            print(f'{key}: {value}')
        print("===================")

    def get_user_choice(self):
        """Получает выбор пользователя."""
        while True:
            choice = input("Выберите пункт меню: ")
            if Menu.is_valid_choice(choice, self.items):
                return int(choice)
            else:
                print("Некорректный ввод. Пожалуйста, выберите существующий пункт меню.")
    
    def get_menu_action(self):
        """
        Возвращает название выбранного пользователем пункта меню.
        :return: Название выбранного пункта меню.
        """
        choice = self.get_user_choice()
        return self.items[choice]
    
    @staticmethod
    def is_valid_choice(choice, menu_items):
        return choice.isdigit() and int(choice) in menu_items