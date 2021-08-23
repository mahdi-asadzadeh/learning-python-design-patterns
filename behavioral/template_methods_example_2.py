from abc import ABC, abstractmethod


class AbstracClass(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def operation1(self):
        pass
    
    @abstractmethod
    def operation2(self):
        pass

    @abstractmethod
    def operation3(self):
        pass

    def template_method(self):
        self.operation1()
        self.operation2()
        self.operation3()


class ConcreteClass(AbstracClass):

    def operation1(self):
        print('operation 1 ...')
    
    def operation2(self):
        print('operation 2 ...')

    def operation3(self):
        print('operation 3 ...')


# Client
if __name__ == '__main__':
    concrete_class = ConcreteClass()
    concrete_class.template_method()