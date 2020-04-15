from store.exceptions import PriceError


class Product:
    """
    Returns object of product.
    """
    def __init__(self, title, price):
        if int(price) > 1000 or int(price) <= 0:
            raise PriceError('The price is incorrect.')
        self.title = title
        self.price = int(price)