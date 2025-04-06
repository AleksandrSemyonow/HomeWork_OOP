from src.products import Product


class Category:
    """Класс для предоставления категорий товаров"""

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        """Метод для инициализации экземпляра класса"""

        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    @property
    def add_product(self) -> str:
        """Возвращает список товара в виде строки"""
        product_str = ""
        for product in self.__products:
            product_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"

        return product_str

    @add_product.setter
    def add_product(self, new_product):
        """Добавляет продукт в список продуктов категории"""
        if isinstance(new_product, Product):
            self.__products.append(new_product)
            self.product_count += 1
        else:
            raise TypeError

    @property
    def add_in_product(self):
        return self.__products
