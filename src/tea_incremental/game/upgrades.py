'''All upgrades.'''

from abc import ABC
from typing import List

class Upgrade(ABC):

    def __init__(self, price, rate, name, description):
        self.price = price
        self.rate = rate
        self.name = name
        self.description = description
        self.active = False

    def activate(self):
        self.active = True

    def __copy__(self):
        copy = self.__class__(self.price, self.rate, self.name, self.description)
        copy.active = self.active
        return copy

UPGRADES: List[Upgrade] = []

def add_upgrade(cls):
    '''Add upgrade to list of upgrades.'''

    UPGRADES.append(cls())

    return cls

@add_upgrade
class WateringCan(Upgrade):

    def __init__(self):
        super().__init__(10.0, 0.05, "Watering Can", "A watering can for your tea trees!")