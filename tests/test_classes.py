"""Модуль с тестами для проверки классов товаров и категорий."""
from main import Product, Category


def test_product_init(product_iphone):
    """ Тест инициализации товара (имя, описание, цена, количество)"""
    assert product_iphone.name == "Iphone 15"
    assert product_iphone.description == "512GB, Blue"
    assert product_iphone.price == 210000.0
    assert product_iphone.quantity == 5


def test_category_init(category_electronics):
    """Тест инициализации категории и корректности счетчиков"""
    assert category_electronics.name == "Электроника"
    assert category_electronics.description == "Гаджеты"
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_price_setter_invalid(product_samsung):
    """ Тест сеттера цены: проверка запрета на отрицательную цену"""
    initial_price = product_samsung.price
    product_samsung.price = -1000.0
    # Цена не должна измениться, так как сработала проверка в сеттере
    assert product_samsung.price == initial_price

    product_samsung.price = 0
    assert product_samsung.price == initial_price


def test_category_products_property(category_electronics):
    """Тест геттера products: проверка формата вывода списка товаров"""
    # Ожидаем строку на основе данных из фикстур product_iphone и product_samsung
    expected_output = (
        "Iphone 15, 210000 руб. Остаток: 5 шт.\n"
        "Samsung Galaxy S23, 180000 руб. Остаток: 10 шт.\n"
    )
    assert category_electronics.products == expected_output

