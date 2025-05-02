
class Hotel:
    def __init__(self, hotel_id: int, name:str, stars:int, adresse):
        self.__hotel_id = hotel_id
        self.__name = name
        self.__stars = stars
        self.__adresse = adresse
    @property
    def hotel_id(self):
        return self.__hotel_id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def stars(self):
        return self.__stars
    @stars.setter
    def stars(self, stars):
        self.__stars = stars

    @property
    def adresse(self):
        return self.__adresse
    @adresse.setter
    def adresse(self, adresse):
        self.__adresse = adresse

