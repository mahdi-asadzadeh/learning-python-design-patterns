# Facade
# ==========================================================================
# ==========================================================================
class EventManager:
    def __init__(self):
        self.presenter = Presenter()
        self.theater_group = TheaterGroup()

    def arrange(self):
        self.presenter.set_presenter()
        self.theater_group.set_theater()
    

# Subsystems
# ==========================================================================
# ==========================================================================


class Presenter:
    def set_presenter(self):
        print('set presenter.') 


class TheaterGroup:
    def set_theater(self):
        print('set theater.')


# Client
# ==========================================================================
# ==========================================================================


def client_code(event_facade: EventManager):
    event_facade.arrange()


if __name__ == '__main__':
    client_code(EventManager())
