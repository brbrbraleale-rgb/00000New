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

    product_samsung.price = 0
    assert product_samsung.price == initial_price

def test_category_count(category_electronics: Category) -> None:
    """Проверка подсчета количества категорий"""
    # Сбрасываем счетчик для чистоты теста, если это необходимо,
    assert Category.category_count >= 1

def test_category_products_property(category_electronics):
    """Тест геттера products: проверка формата вывода списка товаров"""
    # Ожидаем строку на основе данных из фикстур product_iphone и product_samsung
    expected_output = (
        "Iphone 15, 210000 руб. Остаток: 5 шт.\n"
        "Samsung Galaxy S23, 180000 руб. Остаток: 10 шт.\n"
    )
    assert category_electronics.products == expected_output

def test_product_count(category_electronics: Category) -> None:
    """Проверка подсчета количества продуктов"""
    assert Category.product_count >= 2



def test_product_str(product_iphone: Product) -> None:
    """Проверка строкового отображения продукта (__str__)"""
    assert str(product_iphone) == "Iphone 15, 210000.0 руб. Остаток: 5 шт."


def test_category_str(category_electronics: Category) -> None:
    """Проверка строкового отображения категории (__str__)"""
    assert str(category_electronics) == "Электроника, количество продуктов: 15 шт."

