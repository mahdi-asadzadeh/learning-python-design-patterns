from abc import ABC, abstractmethod


# Abstract class
class Compiler(ABC):

    @abstractmethod
    def collect_source(self):
        pass
    
    @abstractmethod
    def compiler_to_object(self):
        pass

    @abstractmethod
    def run(self):
        pass
    
    # Template Method
    def compile_and_run(self):
        self.collect_source()
        self.compiler_to_object()
        self.run()


# Concrete class
class IOSCompiler(Compiler):

    def collect_source(self):
        print('Collecting source code .')

    def compiler_to_object(self):
        print('Compiling source code to obj code.')

    def run(self):
        print('Program running.')


# Client
if __name__ == '__main__':
    ios_compiler = IOSCompiler()
    ios_compiler.compile_and_run()
            