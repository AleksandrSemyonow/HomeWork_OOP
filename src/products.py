from typing import Union


class Product:
    """Класс для представления товара"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Метод для инициализации экземпляра класса"""

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_dict: dict) -> "Product":
        """Создаёт новый экземпляр класса Product из словаря"""
        return cls(**product_dict)

    @property
    def price(self) -> float:
        """Возвращает цену товара"""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Возвращает сообщение об ошибке, если цена меньше или равна нулю"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price
