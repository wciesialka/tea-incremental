import datetime
from time import sleep, time
import os

from tea_incremental.game.producers import TeaTree
from tea_incremental.game.upgrades import WateringCan

class StopGame:
    pass

class TeaGame:

    FRAMES_PER_SECOND: float = 1
    GLOBAL_RATE: float = 1/FRAMES_PER_SECOND

    def __init__(self):
        self.start = datetime.datetime.now()
        self.end_time = None
        self.running = True
        self.leaves = 0
        self.cash = 1
        self.producers = [TeaTree()]
        self.upgrades = [WateringCan()]

    def list_producers(self):
        for i,producer in enumerate(self.producers):
            print(f"[{i}] {producer.name} - ${producer.price:0.2f}\n{producer.description}\nProduces {producer.production} leaves per second.")

    def purchase_producer(self, producer):
        if(producer.price <= self.cash):
            producer.count = producer.count + 1
            self.cash -= producer.price
            producer.raise_price()
        else:
            print("You cannot afford this purchase!")

    def purchase_upgrade(self, upgrade):
        if(upgrade.price <= self.cash):
            self.cash -= upgrade.price
            upgrade.activate()
        else:
            print("You cannot afford this purchase!")  

    def game_loop(self):
        sleep(TeaGame.GLOBAL_RATE)
        
        production_rate = 1
        for upgrade in self.upgrades:
            if upgrade.active:
                production_rate += upgrade.rate
        for producer in self.producers:
            self.leaves += producer.production * producer.count * production_rate * TeaGame.GLOBAL_RATE

    def stop(self):
        raise StopGame

    def dispose(self):
        self.end_time = datetime.datetime.now()
        
    def __del__(self):
        self.dispose()