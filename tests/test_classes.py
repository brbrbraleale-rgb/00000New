"""Тесты"""
from main import Product, Category

def test_product_init(product_iphone: Product) -> None:
    """Проверка инициализации Product"""
    assert product_iphone.name == "Iphone 15"
    assert product_iphone.description == "512GB, Blue"
    assert product_iphone.price == 210000.0
    assert product_iphone.quantity == 5


def test_category_init(category_electronics: Category) -> None:
    """Проверка инициализации Category"""
    assert category_electronics.name == "Электроника"
    assert category_electronics.description == "Гаджеты"
    assert len(category_electronics.products) == 2


def test_category_count(category_electronics: Category) -> None:
    """Проверка подсчета количества категорий"""
    assert category_electronics.category_count == 1
    # Создаем еще одну, чтобы проверить инкремент
    Category("Одежда", "Описание", [])
    assert Category.category_count == 2


def test_product_count(category_electronics: Category) -> None:
    """Проверка подсчета количества продуктов"""
    # В фикстуре category_electronics два продукта
    assert category_electronics.product_count == 2
