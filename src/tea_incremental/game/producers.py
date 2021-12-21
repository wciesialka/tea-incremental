from abc import ABC, abstractmethod

class Producer(ABC):

    def __init__(self, price, tps, name, description):
        self.price = price
        self.production = tps
        self.count = 0
        self.name = name
        self.description = description

    @abstractmethod
    def price_formula(self):
        pass 

    def raise_price(self):
        self.price = self.price_formula()

class TeaTree(Producer):

    def __init__(self):
        super().__init__(1.0, 0.25, "Tea Tree", "A young tea tree.")

    def price_formula(self):
        return self.price ** 1.05