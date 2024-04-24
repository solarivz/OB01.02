# *Дополнительное задание:
# Ты разрабатываешь программное обеспечение для сети магазинов.
# Каждый магазин в этой сети имеет свои особенности, но также
# существуют общие характеристики, такие как адрес, название и
# ассортимент товаров. Ваша задача — создать класс `Store`,
# который можно будет использовать для создания различных магазинов.

# Шаги:
# 1. Создай класс `Store`:
# -Атрибуты класса:
#
# - `name`: название магазина.
# - `address`: адрес магазина.
# - `items`: словарь, где ключ - название товара, а значение - его цена.
# Например, `{'apples': 0.5, 'bananas': 0.75}`.

# - Методы класса:
# - `__init__ - конструктор, который инициализирует название и адрес, а # также пустой словарь
# для `items`.
#
# - метод для добавления товара в ассортимент.
# - метод для удаления товара из ассортимента.
# - метод для получения цены товара по его названию. Если товар отсутствует, возвращайте `None`.
# - метод для обновления цены товара.
#
# 2. Создай несколько объектов класса `Store`:
# Создай не менее трех различных магазинов с разными названиями, адресами и
# добавь в каждый из них несколько товаров.
import random

class Store():
    stores = []

    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

        # Добавляем созданный экземпляр в список всех магазинов
        Store.stores.append(self)

    def add_item(self, product, price):
        self.items[product] = price
        print(f"Товар '{product}' добавлен в список по цене {price} руб.\n")

    def get_price(self, name):
        return self.items.get(name)

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
            print(f"Товар '{name}' удален из ассортимента.\n")
        else:
            print(f"Товар '{name}' отсутствует в ассортименте.\n")

    def update_price(self, name, new_price):
        if name in self.items:
            self.items[name] = new_price
            print(f"Цена товара '{name}' обновлена до {new_price} руб.\n")
        else:
            print(f"Товар '{name}' отсутствует в ассортименте.\n")


# Создаем экземпляры класса Store и добавляем товары
store1 = Store('Ягодка', 'г.Иваново, ул.Солнечная д.1')
product_names = ["Яблоки", "Бананы", "Молоко", "Хлеб", "Кофе", "Чай", "Масло", "Сахар", "Мясо", "Рыба"]
for product in product_names:
    price = round(random.uniform(10.0, 100.0), 2)
    store1.add_item(product, price)

store2 = Store('Хлебушек', 'г.Иваново, ул.Дальняя д.26')
store2.add_item('Бородинский хлеб 250 грамм', 46.50)
store2.add_item('Дарницкий хлеб 350 грамм', 50.50)
store2.add_item('Славянский хлеб 500 грамм', 60.45)
store2.add_item('Кекс с творогом 150 грамм', 25.50)

store3 = Store('Все для дома', 'г.Иваново, пр-кт.Строителей д.101')
product_names = ["Цемент", "Кирпич", "Песок", "Щебень", "Строительный раствор",
    "Гипсокартон", "Краска", "Плитка", "Дверь", "Ламинат"]
for product in product_names:
    price = round(random.uniform(60.0, 800.0), 2)
    store3.add_item(product, price)


# Работа с методами и функциями
# Печать ассортимента всех магазинов
print("Ассортимент всех магазинов:")
for store in Store.stores:
    print(f"Магазин: {store.name}")
    print("Ассортимент:")
    for product, price in store.items.items():
        print(f"Товар: {product}, Цена: {price} руб.")
    print()

# Выводим список всех созданных магазинов
print("Список магазинов:")
for s, store in enumerate(Store.stores, 1):
    print(s, store.name)

# Получаем цену товара в конкретном магазине
store_name = input("Введите название магазина: ")


product_name = input("Введите название товара: ")
price = None
for store in Store.stores:
    if store.name == store_name:
        price = store.get_price(product_name)
        break

if price is not None:
    print(f"Цена товара '{product_name}' в магазине '{store_name}': {price} руб.")
else:
    print(f"Товар '{product_name}' отсутствует в магазине '{store_name}'.")

# Удаляем товар из одного из магазинов
store1.remove_item("Яблоки")

# Обновляем цену товара в одном из магазинов
store3.update_price("Кирпич", 250.0)