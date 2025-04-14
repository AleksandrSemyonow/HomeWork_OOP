from src.category import Category
from src.products import Product


class ProductIterator:

    def __init__(self, category_obj):
        self.category = category_obj
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    @property
    def __next__(self):
        if self.index < len(self.category.add_in_product):
            product = self.category.add_in_product[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
