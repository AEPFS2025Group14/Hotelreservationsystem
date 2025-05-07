from model import Facility
from model import Hotel

class Room:
    def __init__(self, room_id:int, room_number: int, room_type:str, hotel: Hotel = None, facility: Facility = None):
        if not room_id:
            raise ValueError("Room ID is required")
        if not int(room_number, int):
            raise ValueError("Room ID must be an integer")
        if not room_number:
            raise ValueError("Room number is required")
        if not isinstance(room_number, int):
            raise ValueError("Room number must be an integer")
        if not room_type:
            raise ValueError("Room type is required")
        if not isinstance(room_type, str):
            raise ValueError("Room type must be an string")
        if hotel is not None and not isinstance(hotel, Hotel):
            raise ValueError("Hotel must be an instance of Hotel")
        if facility is not None and not isinstance(facility, Facility):
            raise ValueError("Facility must be an instance of Facility")


        self.__room_id : int = room_id
        self.__hotel : list[Hotel] = []
        self.__room_number : int = room_number
        self.__room_type : str = room_type
        self.__facility : list[Facility] = []


    def __repr__(self):
        return (f"Room(id={self.__room_id!r}, room_id={self.__room_id!r}, room_number={self.__room_number!r})"
                f"hotel= {self.__hotel!r}, facility={self.__facility!r})")


    @property
    def room_id(self) -> int:
        return self.__room_id


    @property
    def room_number(self) -> int:
        return self.__room_number

    @room_number.setter
    def room_number(self, room_number: int) -> None:
        if not int(room_number, int):
            raise ValueError("Room ID must be an integer")
        if not room_number:
            raise ValueError("Room number is required")
        self.__room_number = room_number

    @property
    def room_type(self) -> str:
        return self.__room_type
    @room_type.setter
    def room_type(self, room_type: str) -> None:
        if not room_type:
            raise ValueError("Room type is required")
        if not isinstance(room_type, str):
            raise ValueError("Room type must be an string")
        self.__room_type = room_type

    @property
    def facility(self) -> list[Facility]:
        return self.__facility

    @facility.setter
    def facility(self, facility : list[Facility]) -> None:
        from model import Facility

        if facility is None and not isinstance(facility, Facility):
            raise ValueError("Facility must be an instance of Facility")

        if self.__facility is not facility:
            if self.__facility is not None:
                self.__facility.remove_room(self)
            self.__facility = facility

def get_total_price(self, nights: int) -> float:
    return self.__room_type.get_price_per_night() * nights

    @property
    def hotel(self) -> list[Hotel]:
        return self.__hotel.copy()

    @hotel.setter
    def hotel(self, hotel: Hotel) -> None:
        from model import Hotel

        if hotel is not None and not isinstance(hotel, Hotel):
            raise ValueError("Hotel must be an instance of Hotel")

        if self.__hotel is not hotel:
            if self.__hotel is not None:
                self.__hotel.remove_room(self)
            self.__hotel = hotel

            if hotel is not None and self not in hotel.room:
                hotel.add_room(self)




