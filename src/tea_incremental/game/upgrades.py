from abc import ABC

class Upgrade(ABC):

    def __init__(self, price, rate, name, description):
        self.price = price
        self.rate = rate
        self.name = name
        self.description = description
        self.active = False

    def activate(self):
        self.active = True

class WateringCan(Upgrade):

    def __init__(self):
        super().__init__(10.0, 0.05, "Watering Can", "A watering can for your tea trees!")