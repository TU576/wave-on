class HardwareStore:
    def __init__(self, name):
        self.name = name
        # Словарь для хранения товаров: {'название': {'price': цена, 'quantity': количество}}
        self.inventory = {
            "Молоток":{"price": 750, "quantity": 30},
            "Гвозди":{"price": 30, "quantity": 750},
            "ПВА клей":{"price": 300, "quantity": 25},
            "Отвертка":{"price": 250, "quantity": 350}
        }
        
    #git add name file 
    #git commit -m "I add new function future"
    #git push 
    def trading(self):
        shopping_list = []
        item = True
        for item in range ():
            product = input("Введите продукты:")
            shopping_list.append(product)
        for item in shopping_list:
            print("Список продуктов:", item) 

    def filtration(self):
        categories_keywords = {
            "Электроника": ["Дрель", "Шуруповёрт", "Лампочка", "Провод", "Розетка"],
            "Садовые вещи": ["Лопата", "Веник", "Тяпка", "Вила", "Грабли"],
        }

        