"""Тесты"""

from main import Category, Product


def test_product_init_and_price_setter(product_iphone: Product) -> None:
    """Тест 1: Проверка базовой инициализации и работы сеттера цены (Задание 4)"""
    assert product_iphone.name == "Iphone 15"
    assert product_iphone.price == 210000.0

    # Проверяем работу сеттера
    product_iphone.price = 250000.0
    assert product_iphone.price == 250000.0

    # Проверяем защиту от некорректной цены
    product_iphone.price = -1000
    assert (
        product_iphone.price == 250000.0
    )  # Цена не должна была измениться


def test_new_product_from_dict() -> None:
    """Тест 2: Проверка создания продукта из словаря через класс-метод"""
    data = {
        "name": "Xiaomi Redmi Note 11",
        "description": "1024GB, Синий",
        "price": 31000.0,
        "quantity": 14,
    }
    # Вызываем класс-метод
    new_prod = Product.new_product(data)

    assert new_prod.name == "Xiaomi Redmi Note 11"
    assert new_prod.price == 31000.0
    assert new_prod.quantity == 14


def test_category_add_product_and_counts(
    category_electronics: Category,
) -> None:
    """Тест проверка добавления продукта и работы счетчиков"""
    # в фикстуре category_electronics изначально 2 товара
    initial_count = Category.product_count

    # Создаем новый товар и добавляем через специальный метод
    new_item = Product("Тестовый гаджет", "Описание", 1000.0, 1)
    category_electronics.add_product(new_item)

    # Проверяем, что счетчик увеличился ровно на 1
    assert Category.product_count == initial_count + 1


def test_category_products_output(category_electronics: Category) -> None:
    """Тест 4: Проверка вывода товаров в виде строки через property (Задание 2)"""
    # мы проверим, что геттер возвращает строку и она не пустая.
    products_string = category_electronics.products

    assert isinstance(products_string, str)
    # Проверяем, что в строке есть ключевые слова из шаблона
    assert "руб. Остаток:" in products_string

