import json

class TaxFinesDB:
    def __init__(self, filename="fines_db.json"):
        self.filename = filename
        self.database = {}
        self.load_database()

    def load_database(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                self.database = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.database = {}

    def save_database(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(self.database, file, indent=4, ensure_ascii=False)

    def add_person(self, iin, name, city):
        if iin in self.database:
            print("Человек с таким ИИН уже существует.")
        else:
            self.database[iin] = {"name": name, "city": city, "fines": []}
            print("Человек добавлен успешно.")
            self.save_database()

    def add_fine(self, iin, fine_type, amount):
        if iin in self.database:
            self.database[iin]["fines"].append({"type": fine_type, "amount": amount})
            print("Штраф добавлен.")
            self.save_database()
        else:
            print("Человек с таким ИИН не найден.")

    def remove_fine(self, iin, fine_index):
        if iin in self.database and 0 <= fine_index < len(self.database[iin]["fines"]):
            del self.database[iin]["fines"][fine_index]
            print("Штраф удален.")
            self.save_database()
        else:
            print("Ошибка: штраф не найден.")

    def edit_person(self, iin, name=None, city=None):
        if iin in self.database:
            if name:
                self.database[iin]["name"] = name
            if city:
                self.database[iin]["city"] = city
            print("Данные обновлены.")
            self.save_database()
        else:
            print("Человек не найден.")

    def edit_fine(self, iin, fine_index, fine_type=None, amount=None):
        if iin in self.database and 0 <= fine_index < len(self.database[iin]["fines"]):
            if fine_type:
                self.database[iin]["fines"][fine_index]["type"] = fine_type
            if amount:
                self.database[iin]["fines"][fine_index]["amount"] = amount
            print("Штраф обновлен.")
            self.save_database()
        else:
            print("Ошибка: штраф не найден.")

    def print_all(self):
        print(json.dumps(self.database))

    def print_person(self, iin):
        if iin in self.database:
            print(json.dumps(self.database[iin]))
        else:
            print("Человек не найден.")

   
    def print_by_city(self, city):
        result = {iin: data for iin, data in self.database.items() if data["city"] == city}
        print(json.dumps(result, indent=4, ensure_ascii=False))


def menu():
    db = TaxFinesDB()
    while True:
        print("""
        1. Показать всю базу данных
        2. Найти человека по ИИН
        3. Найти штрафы по типу
        4. Найти штрафы по городу
        5. Добавить человека
        6. Добавить штраф
        7. Удалить штраф
        8. Редактировать данные человека
        9. Редактировать штраф
        10. Выход
        """)
        
        choice = input("Выберите действие: ")
        match choice:
            case "1":
                db.print_all()
            case "2":
                iin = input("Введите ИИН: ")
                db.print_person(iin)
            case "3":
                city = input("Введите город: ")
                db.print_by_city(city)
            case "4":
                iin = input("Введите ИИН: ")
                name = input("Введите имя: ")
                city = input("Введите город: ")
                db.add_person(iin, name, city)
            case "5":
                iin = input("Введите ИИН: ")
                fine_type = input("Введите тип штрафа: ")
                amount = float(input("Введите сумму штрафа: "))
                db.add_fine(iin, fine_type, amount)
            case "6":
                iin = input("Введите ИИН: ")
                fine_index = int(input("Введите индекс штрафа: "))
                db.remove_fine(iin, fine_index)
            case "7":
                iin = input("Введите ИИН: ")
                name = input("Введите новое имя (оставьте пустым, если не меняется): ")
                city = input("Введите новый город (оставьте пустым, если не меняется): ")
                db.edit_person(iin, name or None, city or None)
            case "8":
                iin = input("Введите ИИН: ")
                fine_index = int(input("Введите индекс штрафа: "))
                fine_type = input("Введите новый тип штрафа (оставьте пустым, если не меняется): ")
                amount = input("Введите новую сумму штрафа (оставьте пустым, если не меняется): ")
                db.edit_fine(iin, fine_index, fine_type or None, float(amount) if amount else None)
            case "0":
                break
menu()