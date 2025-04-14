from src.smartphone import Smartphone


def test_smartphone_init(product_smartphone: Smartphone):
    """Тестируем инициализацию объекта класса Smartphone"""
    assert product_smartphone.name == "Samsung Galaxy S23 Ultra"
    assert product_smartphone.model == "S23 Ultra"
    assert product_smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert product_smartphone.memory == 256
    assert product_smartphone.efficiency == 95.5
    assert product_smartphone.color == "Серый"
    assert product_smartphone.price == 180000.0
    assert product_smartphone.quantity == 5
