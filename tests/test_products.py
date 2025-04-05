from src.products import Product


def test_products(first_product):
    assert first_product.name == "Samsung"
    assert first_product.description == "256GB, Серый цвет, 200MP камера"
    assert first_product.price == 180000.0
    assert first_product.quantity == 5


def test_product_new_product():
    product = {"name": "Nokia", "description": "Yellow", "price": 90000.0, "quantity": 10}
    new_product = Product.new_product(product)
    assert new_product.name == "Nokia"
    assert new_product.description == "Yellow"
    assert new_product.price == 90000.0
    assert new_product.quantity == 10


def test_price_property(product):
    assert product.price == 180000.0


def test_price_setter(capsys, product):
    product.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
    assert product.price == 180000.0

    product.price = -99999.0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
    assert product.price == 180000.0

    product.price = 0.1
    assert product.price == 0.1
