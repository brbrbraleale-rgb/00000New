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
        # Формируем красивый вывод: ИмяКласса('аргумент1', 'аргумент2', ...)
        properties = ", ".join([f"'{v}'" if isinstance(v, str) else str(v) for v in self.__dict__.values()])
        return f"{self.__class__.__name__}({properties})"


class Product(PrintableMixin, BaseProduct):
    """Класс для представления товара"""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        super().__init__(name, description, price, quantity)

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Сложение товаров только одного класса через проверку type()"""
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


if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                         [product4])

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)
