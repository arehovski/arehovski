from exceptions import PriceError

class Product:
    def __init__(self, title, price):
        if int(price) > 1000 or int(price) <= 0:
            raise PriceError('The price is incorrect.')
        self.title = title
        self.price = int(price)