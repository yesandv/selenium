class RubberDuck:
    def __init__(self, name=None, price=None, discount_price=None):
        self.name = name
        self.price = price
        self.discount_price = discount_price

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price and self.discount_price == other.discount_price

    def __repr__(self):
        return f"Rubber Duck: name='{self.name}', price={self.price}, discount_price={self.discount_price}"
