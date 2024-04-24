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


class Store():
    def __init__(self, name, address):
        self.name  = name                   # название магазина.
        self.address = address              # адрес магазина.
        self.items = {}                     # словарь апример, {'apples': 0.5, 'bananas': 0.75}.

    def add_item(self, product, price):
        items[product] = price
        print(f"Товар '{product_name}' добавлен в список по цене {price}.\n")


magazine1 = Store('Ягодка', 'г.Иваново, ул.Солнечная д.1')

magazine1.add_item('яблоки', 80.00)