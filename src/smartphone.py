from src.products import Product


class Smartphone(Product):
    """Класс - наследник, класса Product"""

    def __init__(self, name, model, description, memory, efficiency, color, price, quantity):
        super().__init__(name, description, price, quantity)
        self.model = model
        self.memory = memory
        self.efficiency = efficiency
        self.color = color
