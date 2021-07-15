from abc import ABC, abstractmethod


class AbstractOperation(ABC):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        super().__init__()

    @abstractmethod
    def execute(self):
        pass


class AddOperation(AbstractOperation):
    def execute(self):
        return self.a + self.b


class MultiplyOperation(AbstractOperation):
    def execute(self):
        return self.a * self.b


add_operation = AddOperation(1, 2)
print(add_operation.execute())


multiply_operation = MultiplyOperation(2, 5)
print(multiply_operation.execute())
