class Subject:
    def __init__(self):
        self.__observers = []

    def register(self, observer):
        self.__observers.append(observer)
    
    def notify_every_one(self, *args, **kwargs):
        for observer in  self.__observers:
            observer.notify(self, *args, **kwargs)


class Observer1:
    def __init__(self, subject):
        subject.register(self)
    
    def notify(self, subject, *args):
        print(type(self).__name__, args, subject)


class Observer2:
    def __init__(self, subject):
        subject.register(self)
    
    def notify(self, subject, *args):
        print(type(self).__name__, args, subject)
            

sub = Subject()
observer1 = Observer1(sub)
observer2 = Observer2(sub)
sub.notify_every_one('Warning.')
