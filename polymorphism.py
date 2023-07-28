from abc import ABC, abstractmethod


class AbstractService(ABC):

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


class ProductService(AbstractService):

    def read(self, identifier):
        return identifier

    def update(self, data, identifier):
        return data, identifier

    def create(self, data):
        return data

    def delete(self, identifier):
        return identifier


class EducationService(AbstractService):

    def read(self, identifier):
        return identifier

    def update(self, data, identifier):
        return data, identifier

    def create(self, data):
        return data

    def delete(self, identifier):
        return identifier


# polymorphism
def create_crud_operations(service: AbstractService):
    return {
        'read': service.read,
        'create': service.create,
        'update': service.update,
        'delete': service.delete
    }

product_service = ProductService()
education_service = EducationService()

# di
crud_product = create_crud_operations(product_service)
crud_education = create_crud_operations(education_service)

print(crud_product['delete'](1))
print(crud_education['delete'](2))