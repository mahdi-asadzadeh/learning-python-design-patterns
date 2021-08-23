from abc import ABC, abstractmethod


# command 
class Order(ABC):

    @abstractmethod
    def execute(self):
        pass


# Concrete command
class BuyHouse(Order):

    def __init__(self, house):
        self.house = house
    
    def execute(self):
        self.house.buy()


# Concrete command
class SellHouse(Order):
    def __init__(self, house):
        self.house = house
    
    def execute(self):
        self.house.sell()


# Reciever
class HouseTrade:
    def buy(self):
        print('buy house.')
    
    def sell(self):
        print('sell house')


class Agent:

    def __init__(self):
        self.order_queue = []

    def place_order(self, order):
        self.order_queue.append(order)
        order.execute()


# Client
if __name__ == '__main__':
    house = HouseTrade()
    buy_house = BuyHouse(house)
    sell_house = SellHouse(house)
    agent = Agent()
    agent.place_order(buy_house)