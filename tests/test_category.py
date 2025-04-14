import pytest

from src.category import Category


def test_product_init(product):
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_category_init(category_1, category_2):
    assert category_1.name == "Смартфоны"
    assert category_1.description == (
        "Смартфоны, как средство не только коммуникации, " "но и получения дополнительных функций для удобства жизни"
    )
    assert len(category_1.add_in_product) == 2

    assert Category.category_count == 2
    assert category_1.category_count == 2
    assert category_2.category_count == 2

    assert category_1.product_count == 3
    assert category_2.product_count == 3
    assert Category.product_count == 3


def test_category_products_list_property(category_1):
    assert category_1.add_product == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
    )


def test_category_products_setter(category_1, product):
    assert len(category_1.add_in_product) == 2
    category_1.add_product = product
    assert len(category_1.add_in_product) == 3


def test_str_category(product):
    assert str(product) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_category_add_product_invalid(category_1: Category) -> None:
    """Тестируем поведение метода добавления продукта в атрибут products при попытке добавить вместо
    продукта другой объект - вызываем ошибку"""
    with pytest.raises(TypeError):
        category_1.add_product("not a product")


def test_middle_price(category_1, category_without_product):
    assert category_1.middle_price() == 198461.54
    assert category_without_product.middle_price() == 0
