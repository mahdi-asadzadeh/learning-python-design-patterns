class Model:
    products = {
        'mobile': {'price': 25000},
        'car': {'price': 25000},
        'file': {'price': 25000},
    }


class View:

    def list_products(self, products):
        for product in products:
            print(product, '')
    
    def list_price(self, products):
        for product in products:
            print(product, '------', Model.products[product]['price'])


class Controller:

    def __init__(self):
        self.model = Model()
        self.view = View()
    
    def get_products(self):
        products = self.model.products.keys()
        return self.view.list_products(products)

    def get_price(self):
        products = self.model.products.keys()
        return self.view.list_price(products)


# Client
if __name__ == '__main__':
    controller = Controller()
    controller.get_products()
    controller.get_price()

