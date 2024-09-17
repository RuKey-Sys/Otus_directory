class Contact():
    def __init__(self, name, number, description):
        self.name = name
        self.number = number
        self.description = description

    def show_contact(self):
        return f"{self.number:<15}{self.name:<10}{
              self.description:<20}"
    
    def change_contact(self, value: dict):
        self.name = value["name"]
        self.number = value["phone"]
        self.description = value["description"]

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.number,
            "description": self.description
        }