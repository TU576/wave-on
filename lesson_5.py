class HardwareStore:
    def __init__(self, name):
        self.name = name
        # Словарь для хранения товаров: {'название': {'price': цена, 'quantity': количество}}
        self.inventory = {}
        