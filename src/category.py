from src.products import Product
from src.exceptions import ZeroQuantityProduct


class Category:
    """Класс для предоставления категорий товаров"""
    __products: list

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0
    product_list: list = []

    def __init__(self, name: str, description: str, products: list):
        """Метод для инициализации экземпляра класса"""

        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)
        Category.product_list.extend(products)

    def __str__(self):
        quantity_sum = 0
        if product in self.__products:
            quantity_sum += product.quantity
        return f"{self.name}, количество продуктов: {quantity_sum} шт."

    @property
    def add_product(self) -> str:
        """Возвращает список товара в виде строки"""
        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)}\n"

        return product_str

    @add_product.setter
    def add_product(self, new_product):
        """Добавляет продукт в список продуктов категории"""
        if isinstance(new_product, Product):
            try:
                if new_product.quantity == 0:
                    raise ZeroQuantityProduct("Попытка добавить товар с нулевым количеством")
            except ZeroQuantityProduct as e:
                print(str(e))
            else:
                self.__products.append(new_product)
                Category.product_count += 1
                Category.product_list.append(new_product)
                print("Товар добавлен успешно")
            finally:
                print("Обработка добавления товара завершена")
        else:
            raise TypeError

    @property
    def add_in_product(self):
        return self.__products

    def middle_price(self) -> float:
        """Метод, который подсчитывает средний ценник всех товаров в данной категории"""
        quantity_sum = 0
        price_sum = 0
        for product in self.__products:
            price_sum += product.price * product.quantity
            quantity_sum += product.quantity
        try:
            return round(price_sum / quantity_sum, 2)
        except ZeroDivisionError:
            return 0
