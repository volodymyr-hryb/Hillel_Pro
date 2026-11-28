class Product:
    CATEGORIES = ["Electronics", "Clothing", "Books", "Food"]

    def __init__(self, name, price, quantity, category):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category

    def __str__(self):
        return f"Товар: {self.name} (категорія: {self.category}) — ціна: {self.price} грн, кількість: {self.quantity} шт."

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.name == other.name and self.category == other.category
        return False

    def __lt__(self, other):
        if isinstance(other, Product):
            return self.price < other.price
        return False

    def __add__(self, other):
        if isinstance(other, Product) and self.name == other.name:
            self.quantity += other.quantity
            return self
        else:
            raise ValueError("Не можна об'єднати різні товари.")

    def __mul__(self, other):
        self.quantity *= other
        return self


    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Ціна не може бути від'ємною")
        self._price = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError("Кількість не може бути від'ємною")
        self._quantity = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if value not in self.CATEGORIES:
            raise ValueError("Недопустима категорія товару")
        self._category = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value is None or len(value) == 0:
            raise ValueError("Назва не може бути порожньою")
        self._name = value

    def increase_stock(self, amount):
        if amount <= 0:
            print("Кількість товарів, на яку збільшуються запаси має бути більше нуля.")
        else:
            self.quantity += amount
        return self.quantity

    def decrease_stock(self, amount):
        if amount <= 0:
            print("Кількість товарів, на яку зменшуються запаси має бути більше нуля.")
        elif amount > self.quantity:
            print("Кількість товарів, яка списується більша ніж та, яка є на складі.")
        else:
            self.quantity -= amount
        return self.quantity

    def calculate_total_value(self):
        total_value = self.price * self.quantity
        print(f"Загальна вартість товару на складі: {total_value}.")
        return total_value

product1 = Product(
    "Keyboard",
    1500,
    10,
    "Electronics")
product2 = Product(
    "Keyboard",
    1500,
    5,
    "Electronics")
print(product1 == product2)
print(product1 < product2)
result = product1 + product2
result = product1 * 3

