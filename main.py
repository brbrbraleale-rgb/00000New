"""Модуль для Классов и Категорий"""


class Product:
    """Класс для представления товара"""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.quantity = quantity
        self.price = price  # Используем сеттер для проверки цены

    @property
    def price(self) -> float:
        """Геттер для получения цены"""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для изменения цены с проверкой"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, data: dict):
        """Создание объекта Product из словаря"""
        return cls(
            name=data["name"],
            description=data["description"],
            price=data["price"],
            quantity=data["quantity"],
        )


class Category:
    """Класс для представления категории товаров"""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        self.name = name
        self.description = description
        self.__products = []  # Приватный список

        Category.category_count += 1
        for product in products:
            self.add_product(product)

    def add_product(self, product: Product) -> None:
        """Метод для добавления продукта в приватный список"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Геттер для вывода списка товаров по шаблону"""
        result = ""
        for product in self.__products:
            result += f"{product.name}, {int(product.price)} руб. Остаток: {product.quantity} шт.\n"
        return result


# ПРОВЕРОЧНЫЙ КОД
if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512ГБ, Серое пространство", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий получение", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и дополнительные функции для удобства жизни",
        [product1, product2, product3],
    )

    print(category1.products)

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)

    print(category1.products)
    print(category1.product_count)

    new_product = Product.new_product({
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP camera",
        "price": 180000.0,
        "quantity": 5,
    })

    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    new_product.price = 800
    print(new_product.price)

    new_product.price = -100
    print(new_product.price)

    new_product.price = 0
    print(new_product.price)



