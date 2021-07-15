from abc import ABC, abstractmethod


# Factory
# ==========================================================================
# ==========================================================================


# Abstract Factory
class CoffeeFactory(ABC):

    @abstractmethod
    def create_coffee_with_milk(self):
        pass

    @abstractmethod
    def create_coffee_with_out_milk(self):
        pass


# Concrete Factory
class ItalianCoffeeFactory(CoffeeFactory):
    def create_coffee_with_milk(self):
        return ItalianEspresso()
        
    def create_coffee_with_out_milk(self):
        return ItalianCappucino()


class FrenchCoffeeFactory(CoffeeFactory):
    def create_coffee_with_milk(self):
        return FrenchEspresso()
        
    def create_coffee_with_out_milk(self):
        return FrenchCappucino()


# Product
# ==========================================================================
# ==========================================================================


# Abstract Product
class CoffeeWithMilk(ABC):

    @abstractmethod
    def prepare(self):
        pass


# concrete product
class ItalianCappucino(CoffeeWithMilk):
    def prepare(self):
        return 'italian cappucino with milk.'


# concrete product
class FrenchCappucino(CoffeeWithMilk):
    def prepare(self):
        return 'french cappucino with milk.'


# Abstract Product
class CoffeeWithOutMilk(ABC):

    @abstractmethod
    def prepare(self):
        pass


# concrete product
class ItalianEspresso(CoffeeWithOutMilk):
    def prepare(self):
        return 'italian espresso with out milk.'


# concrete product
class FrenchEspresso(CoffeeWithOutMilk):
    def prepare(self):
        return 'french espresso with out milk.'


# Client
# ==========================================================================
# ==========================================================================


def client_code(factory: CoffeeFactory):
    product_with_milk = factory.create_coffee_with_milk()
    product_with_out_milk = factory.create_coffee_with_out_milk()

    print(product_with_milk.prepare())
    print(product_with_out_milk.prepare())


if __name__ == '__main__':
    client_code(ItalianCoffeeFactory())

    print('*************************************\n')

    client_code(FrenchCoffeeFactory())
