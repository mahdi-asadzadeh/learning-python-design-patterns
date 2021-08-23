from abc import ABC, abstractmethod


# Command
class Command(ABC):

    def __init__(self, receiver):
        self.receiver = receiver
    
    @abstractmethod
    def execute(self):
        pass


# Concrete Command
class ConcreteCommand(Command):
    
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.action()


# Reciever
class Reciever:
    
    def action(self):
        print('Action.')


# Invoker
class Invoker:
    def command(self, command):
        self.command = command

    def execute(self):
        self.command.execute()


if __name__ == '__main__':
    reciever = Reciever()
    command = ConcreteCommand(reciever)
    invoker = Invoker()
    invoker.command(command)
    invoker.execute()
