"""Модуль с фикстурами для тестирования классов Category и Product."""
import pytest
from main import Product, Category, Smartphone, LawnGrass

@pytest.fixture(autouse=True)
def reset_counts() -> None:
    """Сбрасывает счетчики перед каждым тестом, чтобы они не суммировались"""
    Category.category_count = 0
    Category.product_count = 0

@pytest.fixture
def product_iphone() -> Product:
    """Фикстура для смартфона iPhone"""
    return Product("Iphone 15", "512GB, Blue", 210000.0, 5)

@pytest.fixture
def product_samsung() -> Product:
    """Фикстура для смартфона Samsung"""
    return Product("Samsung Galaxy S23", "256GB, Black", 180000.0, 10)

@pytest.fixture
def category_electronics(product_iphone: Product, product_samsung: Product) -> Category:
    """Фикстура для категории электроники"""
    return Category("Электроника", "Гаджеты", [product_iphone, product_samsung])


@pytest.fixture
def smartphone_samsung_ultra():
    """Фикстура для смартфона (наследник)"""
    return Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый")

@pytest.fixture
def grass_green():
    """Фикстура для травы (наследник)"""
    return LawnGrass("Газонная трава", "Элитная", 500.0, 20, "Россия", "7 дней", "Зеленый")
