class Roomtype:

    def __init__(self, room_typ_id:int, description:str, max_guests:int):
        self.__room_typ = room_typ_id
        self.__description = description
        self.__max_guests = max_guests

    @property
    def room_type_id(self):
        return self.__room_typ

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def max_guests(self):
        return self.__max_guests
    @max_guests.setter
    def max_guests(self, max_guests):
        self.__max_guests = max_guests

class RoomType:
    def __init__(self, room_typ_id:int, description:str, max_guests:int, price_per_night:float):
        self.__room_typ = room_typ_id
        self.__description = description
        self.__max_guests = max_guests
        self.__price_per_night = price_per_night

    @property
    def price_per_night(self):
        return self.__price_per_night
