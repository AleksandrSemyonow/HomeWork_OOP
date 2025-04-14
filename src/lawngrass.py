from src.products import Product


class LawnGrass(Product):
    """Класс - наследник, класса Product"""

    def __init__(self, name, description, price, quantity, color, germination_period, country):
        super().__init__(name, description, price, quantity)
        self.color = color
        self.germination_period = germination_period
        self.country = country
