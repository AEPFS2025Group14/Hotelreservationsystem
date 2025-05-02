
class Mensch:
    def __init__(self, last_name:str, first_name:str, email:str, alter:int):
        self.__last_name = last_name
        self.__first_name = first_name
        self.__email = email
        self.__alter = alter

    @property
    def last_name(self):
        return self.__last_name
    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name
    @property
    def first_name(self):
        return self.__first_name
    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email):
        self.__email = email
    @property
    def alter(self):
        return self.__alter
    @alter.setter
    def alter(self, alter):
        self.__alter = alter

