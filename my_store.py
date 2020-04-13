import json


class PriceError(Exception):
    pass


class Product:
    def __init__(self, title, price):
        if int(price) > 1000 or int(price) <= 0:
            raise PriceError('The price is incorrect.')
        self.title = title
        self.price = int(price)


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


class Manager:
    store = None

    @staticmethod
    def create_add_to_store_product():
        Manager.create_store()
        while True:
            msg = input('Would you like to create a product? y/n: ')
            if msg.lower() == 'y':
                product = Manager.create_product()
                product_number = int(input('Type the number of product: '))
                Manager.store.add_product(product, product_number)
            else:
                break
        Manager.store.showcase()
        Manager.dump_data_to_file()

    @staticmethod
    def create_product():
        title = input('Type the name of product: ')
        price = input('Type product price: ')
        try:
            return Product(title, price)
        except PriceError:
            print("Incorrect price. Type again")
            return Manager.create_product()

    @staticmethod
    def create_store():
        if Manager.store is None:
            store_title = input('Type the name of the store: ')
            Manager.store = Store(store_title)
        return Manager.store

    @staticmethod
    def store_info():
        if Manager.store:
            store_info = {'store_title': Manager.store.title,
                          'products': [[key.title, value, key.price] for key, value in Manager.store.products.items()]}
            return store_info
        else:
            print("Can't find any store.")

    @staticmethod
    def dump_data_to_file():
        data_to_json = Manager.store_info()
        with open('my_store.txt', 'w') as w:
            json.dump(data_to_json, w)

    @staticmethod
    def load_data_from_file():
        if not Manager.store:
            with open('my_store.txt', 'r') as r:
                data_from_json = json.load(r)
            Manager.store = Store(data_from_json['store_title'])
            for product in data_from_json['products']:
                classobj = Product(product[0], product[2])
                Manager.store.add_product(classobj, product[1])
            Manager.store.showcase()
        else:
            print('Store has already exist')
            Manager.store.showcase()


if __name__ == '__main__':
    Manager.load_data_from_file()
