'''All producers.'''

from abc import ABC, abstractmethod
from typing import List

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

    def __copy__(self):
        copy = self.__class__(self.price, self.tps, self.name, self.description)
        copy.count = self.count
        return copy


PRODUCERS: List[Producer] = []

def add_producer(cls):

    PRODUCERS.append(cls())
    return cls

@add_producer
class TeaTree(Producer):

    def __init__(self):
        super().__init__(1.0, 0.25, "Tea Tree", "A young tea tree.")

    def price_formula(self):
        return self.price ** 1.05