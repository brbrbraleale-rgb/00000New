from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Базовый абстрактный класс для всех продуктов"""

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class PrintableMixin:
    """Класс-миксин для логирования создания объектов"""

    def __init__(self, *args, **kwargs) -> None:
        # Сначала даем отработать инициализации базовых классов
        super().__init__(*args, **kwargs)
        # Выводим строковое представление объекта в консоль сразу после создания
        print(repr(self))

    def __repr__(self) -> str:
        properties = ", ".join([f"'{v}'" if isinstance(v, str) else str(v) for v in self.__dict__.values()])
        return f"{self.__class__.__name__}({properties})"


class Product(PrintableMixin, BaseProduct):
    """Класс для представления товара"""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

        super().__init__(name, description, price, quantity)

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Сложение товаров только одного класса через проверку"""
        if type(self) is not type(other):
            raise TypeError("Можно складывать только товары одного и того же класса")
        return (self.price * self.quantity) + (other.price * other.quantity)


class Smartphone(Product):
    """Класс Смартфон с доп. атрибутами"""

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: float, model: str, memory: int, color: str) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс Трава газонная с доп. атрибутами"""

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: str, color: str) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class Category:
    """Класс для категорий товаров"""
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product] = None) -> None:
        self.name = name
        self.description = description
        self.__products = []

        if products:
            for product in products:
                self.add_product(product)

        Category.category_count += 1

    def add_product(self, product):
        """Добавление продукта с проверкой на принадлежность к классу Product"""
        if not isinstance(product, Product):
            raise TypeError("Добавлять можно только объекты Product или его наследников")

        self.__products.append(product)
        Category.product_count += 1  # Исправлено имя переменной для работы тестов

    @property
    def products(self):
        return self.__products

    def __str__(self) -> str:
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def middle_price(self) -> float:
        """Подсчитывает средний ценник всех товаров в категории"""
        try:
            total_price = sum(product.price for product in self.__products)
            return total_price / len(self.__products)
        except ZeroDivisionError:
            return 0


if __name__ == '__main__':
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError as e:
        print(
            "Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с нулевым количеством")
    else:
        print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])

    print(category1.middle_price())

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(category_empty.middle_price())