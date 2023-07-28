from abc import ABC, abstractmethod
import json


class AbstractProductService(ABC):

    @abstractmethod
    def read(self, identifier):
        pass

    @abstractmethod
    def create(self, data):
        pass

    @abstractmethod
    def update(self, data, identifier):
        pass

    @abstractmethod
    def delete(self, identifier):
        pass


class ProductService(AbstractProductService):

    def __init__(self):
        self.products = {'data': []}
        self.__load_json()

    def read(self, identifier):
        return next(filter(lambda product: product.get('id') == identifier, self.products['data']), None)

    def create(self, data):

        self.products['data'] = [*self.products['data'], data]

        # updating json file
        self.__update_json()

        return data

    def update(self, data, identifier):
        self.products['data'] = list(map(lambda product: data if product.get(
            'id') == identifier else product, self.products['data']))

        # updating json file
        self.__update_json()

        return self.read(identifier)

    def delete(self, identifier):
        self.products['data'] = list(
            filter(lambda product: product.get('id') != identifier, self.products['data']))

        # updating json file
        self.__update_json()

        return True

    # private method
    def __update_json(self):
        with open('products.json', 'w') as products:
            json.dump(self.products, products)

    # private method
    def __load_json(self):
        try:
            with open('products.json') as products:
                self.products = json.load(products)
        except FileNotFoundError:
            self.products = {'data': []}


# abstraction
product_service = ProductService()
product_service.update({"id": 15, "name": "Wireless Router", "price": 90}, 15)
product_service.delete(15)
product_service.create({"id": 15, "name": "Wireless Router", "price": 90})
print(product_service.products)
