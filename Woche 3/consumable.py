class Consumable:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    tax_rate = 0.19
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, value):
        self.__price = abs(value)


shopping_cart = [Consumable("Apfel", 0.5), Consumable("Brot", -1.5)]
# ──── Zeitpunkt A ────
total_price_before_tax_raise = sum(item.price * (1 + Consumable.tax_rate)
    for item in shopping_cart)

Consumable.tax_rate = 0.25
# ──── Zeitpunkt B ────
total_price_after_tax_raise = sum(item.price * (1 + Consumable.tax_rate)
    for item in shopping_cart)

# ──── Zeitpunkt C ────
print("Total price before tax raise:", round(total_price_before_tax_raise, 2))
print("Total price after tax raise:", round(total_price_after_tax_raise, 2))