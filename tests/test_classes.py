"""Тесты для категорий и классов"""
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
    # Проверка идет через геттер products
    assert len(category_electronics.products) == 2


def test_category_count(category_electronics: Category) -> None:
    """Проверка подсчета количества категорий"""
    # Сбрасываем счетчик для чистоты теста, если это необходимо,
    assert Category.category_count >= 1

def test_category_products_property(category_electronics):
    """Тест геттера products: проверка, что возвращается список объектов"""
    assert len(category_electronics.products) == 2
    assert isinstance(category_electronics.products[0], Product)

def test_product_count(category_electronics: Category) -> None:
    """Проверка подсчета количества продуктов"""
    assert Category.product_count >= 2



def test_product_str(product_iphone: Product) -> None:
    """Проверка строкового отображения продукта (__str__)"""
    assert str(product_iphone) == "Iphone 15, 210000.0 руб. Остаток: 5 шт."


def test_category_str(category_electronics: Category) -> None:
    """Проверка строкового отображения категории (__str__)"""
    assert str(category_electronics) == "Электроника, количество продуктов: 15 шт."


import pytest

def test_products_validation_and_addition(smartphone_samsung_ultra, grass_green):
    """Тест атрибутов наследников и ограничения сложения разных классов"""
    # Проверка атрибутов (Задание 1)
    assert smartphone_samsung_ultra.model == "S23 Ultra"
    assert grass_green.germination_period == "7 дней"

    # Проверка ограничения сложения (Задание 2)
    with pytest.raises(TypeError):
        result = smartphone_samsung_ultra + grass_green


def test_category_add_product_validation(category_electronics, smartphone_samsung_ultra):
    """Тест ограничения добавления в категорию (Задание 3)"""
    # Проверка добавления наследника (успешно)
    initial_count = len(category_electronics.products)
    category_electronics.add_product(smartphone_samsung_ultra)
    assert len(category_electronics.products) == initial_count + 1

    # Проверка добавления некорректного объекта (ошибка)
    with pytest.raises(TypeError):
        category_electronics.add_product("Not a Product")
