import datetime
import random


class RubberDuck:
    def __init__(self, name=None, price=None, discount_price=None):
        self.name = name
        self.price = price
        self.discount_price = discount_price
        self.code = random.randint(000, 999)
        self.category = "Rubber Ducks"
        self.valid_from = datetime.datetime.now()
        self.valid_to = self.valid_from + datetime.timedelta(days=365)
        self.manufacturer = "ACME Corp."

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price and self.discount_price == other.discount_price

    def __repr__(self):
        return f"Rubber Duck: name='{self.name}', price={self.price}, discount_price={self.discount_price}"
