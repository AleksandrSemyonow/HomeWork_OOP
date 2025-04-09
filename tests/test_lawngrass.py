from src.lawngrass import LawnGrass


def test_lawngrass_init(product_grass: LawnGrass):
    """Тестируем инициализацию объекта класса LawnGrass"""
    assert product_grass.name == "Газонная трава"
    assert product_grass.description == "Элитная трава для газона"
    assert product_grass.price == 500.0
    assert product_grass.quantity == 20
    assert product_grass.color == "Зеленый"
    assert product_grass.germination_period == "7 дней"
    assert product_grass.country == "Россия"
