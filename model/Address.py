#Address test

class Address:
    def __init__(self, address_id: int, street:str, city:str, zip_code:str):
        self.__address_id = address_id
        self.__street = street
        self.__city = city
        self.zip_code = zip_code

    @property
    def address_id(self):
        return self.__address_id

    @property
    def street(self):
        return self.__street
    @street.setter
    def street(self, street):
        self.__street = street

    @property
    def city(self):
        return self.__city
    @city.setter
    def city(self, city):
        self.__city = city

    @property
    def zip_code(self):
        return self.__zip_code
    @zip_code.setter
    def zip_code(self, zip_code):
        self.__zip_code = zip_code


