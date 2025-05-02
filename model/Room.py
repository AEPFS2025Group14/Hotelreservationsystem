
class Room:
    def __init__(self, room_id:int, hotel, room_number:int, room_type, facility):
        self.__room_id = room_id
        self.__hotel = hotel
        self.__room_number = room_number
        self.__room_type = room_type
        self.__facility = facility

    @property
    def room_id(self):
        return self.__room_id

    @property
    def hotel(self):
        return self.__hotel

    @hotel.setter
    def hotel(self, hotel):
        self.__hotel = hotel

    @property
    def room_number(self):
        return self.__room_number
    @room_number.setter
    def room_number(self, room_number):
        self.__room_number = room_number

    @property
    def room_type(self):
        return self.__room_type
    @room_type.setter
    def room_type(self, room_type):
        self.__room_type = room_type

    @property
    def facility(self):
        return self.__facility
    @facility.setter
    def facility(self, facility):
        self.__facility = facility
