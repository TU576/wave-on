class HardwareStore:
    def __init__(self, name):
        self.name = name
        # Словарь для хранения товаров: {'название': {'price': цена, 'quantity': количество}}
        self.inventory = {
            "Молоток":{"price": 750, "quantity": 30},
            "Гвозди":{"price": 30, "quantity": 750},
            "ПВА клей":{"price": 300, "quantity": 25},
            "Отвертка":{"price": 250, "quantity": 350},
            "Швабра": {"price": 650, "quantity": 40},
            "Перчатки": {"price": 120, "quantity": 100},
            "Дрель": {"price": 4500, "quantity": 10},
            "Лопата": {"price": 500, "quantity": 20},
            "Веник": {"price": 250, "quantity": 20},
            "Тяпка": {"price": 250, "quantity": 20},
            "Вила": {"price": 250, "quantity": 20},
            "Грабли": {"price": 200, "quantity": 25},
            "Шуруповёрт": {"price": 1500, "quantity": 15},
            "Провод": {"price": 500, "quantity": 25},
            "Розетка": {"price": 240, "quantity": 10},
            "Щётка": {"price": 200, "quantity": 50},
            "Губка": {"price": 120, "quantity": 45},
            "Ведро": {"price": 200, "quantity": 20}
        }

    def show_invventory(self):
        print("Все товары в магазине",  {self.name})


        
    #git add name file 
    #git commit -m "I add new function future"
    #git push 
    def trading(self):
        shopping_list = []
        while True:
            product = input("Введите продукты:")
            if product() == "стоп":
                break
            shopping_list.append(product)
        for item in shopping_list:
            print("Список продуктов:", item) 

    def filtration(self):
        categories_keywords = {
            "Электроника": ["Дрель", "Шуруповёрт", "Провод", "Розетка"],
            "Садовые вещи": ["Лопата", "Веник", "Тяпка", "Вила", "Грабли"],
            "Хозтовар": ["Перчатки", "Щётка", "Губка", "Швабра", "Ведро"],
            "Строй мат.": ["Молоток", "Отвертка", "ПВА клей", "Гвозди"]
        } 

    def web(self):
        store = HardwareStore("Хозмаркет")
        store.web()
        while True:
            print("Меню магазина")
            print("1 - Показать все товары")
            print("2 - Фильтрация по категориям")
            print("3 - Купить товары")
            print("0 - Выйти")

            choice = input("Введите цифру: ")

            if choice == "1":
                self.show_invventory
            elif choice == "2":
                self.filtration
            elif choice == "3":
                self.trading
            elif choice == "0":
                print("Вы вышли из магазина")
                break
            else:
                print("Введите только цифру 0, 1, 2, 3")


        