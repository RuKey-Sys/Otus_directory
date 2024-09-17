import model
import view
from contacts import Contact
from directories import Directory
from menu import Menu 

def start_app():
    # Открываем и считываем справочник
    file_name = view.input_file_name()
    directory = Directory()
    json_data = model.open_file(file_name) if file_name else model.open_file()
    directory.import_data(json_data)
    
    # Создаем главное меню
    main_menu_items = {
        1: "Показать все контакты",
        2: "Создать контакт",
        3: "Найти контакт",
        4: "Выход"
    }
    main_menu = Menu(main_menu_items, "Главное меню")
    
    work_flag = True
    while work_flag:
        # Показываем главное меню
        main_menu.display()
        
        # Читаем выбор пользователя
        selected_action = main_menu.get_menu_action()

        if selected_action == "Показать все контакты":
            view.show_contacts(directory)
        elif selected_action == "Создать контакт":
            input_data = view.create_contact()
            contact = Contact(input_data['name'], input_data['phone'], input_data['description'])
            directory.add_contact(contact)
        elif selected_action == "Найти контакт":
            target_value = view.enter_value()
            found_data = model.find_contact(directory, target_value)
            for i, (key, value) in enumerate(found_data.items()):
                view.show_contact(i, len(found_data), value)
                # Подменю для выбранного контакта
                contact_menu_items = {
                    1: "Изменить контакт",
                    2: "Удалить контакт",
                    3: "Выход"
                }
                contact_menu = Menu(contact_menu_items, "Контактное меню")
                contact_menu.display()
                contact_action = contact_menu.get_menu_action()
                if contact_action == "Изменить контакт":
                    model.change_contact(directory, key, value)
                elif contact_action == "Удалить контакт":
                    model.remove_contact(directory, key, value)
        elif selected_action == "Выход":
            model.exit_directory(directory, file_name) if file_name else model.exit_directory(directory)
            work_flag = False