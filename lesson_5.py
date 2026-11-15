class HardwareStore:
    def __init__(self, name):
        self.name = name
        # Словарь для хранения товаров: {'название': {'price': цена, 'quantity': количество}}
        self.inventory = [
            "Молоток":{"price": 750, "quantity": 30},
            "Гвозди":{"price": 30, "quantity": 750},
            "ПВА клей":{"price": 300, "quantity": 25},
            "Отвертка":{"price": 250, "quantity": 350}
        ]
        
    #git add name file 
    #git commit -m "I add new function future"
    #git push 
    def 