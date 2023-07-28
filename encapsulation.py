class Phone:

    def __init__(self):
        self.__model = 'samsung'

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_model):
        self.__model = new_model


phone = Phone()

phone.model = 'iphone'

print(phone.model)
