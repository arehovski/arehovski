class Store:
    def __init__(self, title):
        self.title = title
        self.products = {}

    def add_product(self, product, number_of_products=1):
        if product in self.products:
            self.products[product] += number_of_products
        else:
            self.products[product] = number_of_products

    def showcase(self, product=None):
        if product:
            print(f'Название магазина: {self.title}')
            print(
                f'Количество товара {product.title.title()}: {self.products[product]} штук, стоимость: {product.price} '
                f'Суммарная стоимость: {product.price * self.products[product]}')

        else:
            print(f'Название магазина: {self.title}')
            for key, value in self.products.items():
                print(f'Количество товара {key.title.title()}: {value} штук, стоимость: {key.price} '
                      f'Суммарная стоимость: {key.price * value}')
