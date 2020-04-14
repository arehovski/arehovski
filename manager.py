import json
from my_store import Store
from exceptions import PriceError
from product import Product


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