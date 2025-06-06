from __future__ import annotations
from typing import TYPE_CHECKING
from model.room_type import RoomType


if TYPE_CHECKING:
    from .room import Room
    from .address import Address
    from model.room_type import RoomType

class Hotel:
    def __init__(self, hotel_id: int, name:str, stars:int, address:Address =None, room_type:RoomType=None):
        if not hotel_id:
            raise ValueError("hotel_id is required")
        if not isinstance(hotel_id, int):
            raise ValueError("hotel_id must be an integer")
        if not name:
            raise ValueError("name is required")
        if not isinstance(name, str):
            raise ValueError("name must be a string")
        if not stars:
            raise ValueError("stars is required")
        if not isinstance(stars, int):
            raise ValueError("stars must be an integer")

        self.__hotel_id: int  = hotel_id
        self.__name: str = name
        self.__stars: int = stars
        self.__address: Address = address
        self.__rooms: list[Room] = []
        self.__room_type: list[RoomType] = []
        if room_type:
            self.add_room_type(room_type)

    def __repr__(self):
        return f"Hotel(id={self.__hotel_id!r}, name={self.__name!r})"

    @property
    def hotel_id(self) -> int:
        return self.__hotel_id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name:str) -> None:
        if not name:
            raise ValueError("name is required")
        if not isinstance(name, str):
            raise ValueError("name must be an string")
        self.__name = name

    @property
    def stars(self) -> int:
        return self.__stars

    @stars.setter
    def stars(self, stars:int) :
        if not stars:
            raise ValueError("stars is required")
        if not isinstance(stars, int):
            raise ValueError("stars must be an integer")
        self.__stars = stars

    @property
    def address(self) -> Address:
        return self.__address

    def add_address(self, address:Address) -> None:
        from .address import Address
        if not address:
            raise ValueError("address is required")
        if not isinstance(address, Address):
            raise ValueError("address must be an instance of Address")
        self.__address = address
        address.hotel = self

    def remove_address(self, address: Address) -> None:
        if self.__address:
            self.__address.hotel = None
        self.__address = None

    @property
    def rooms(self) -> list[Room]:
        return self.__rooms

    def add_room(self, room: Room):
        from .room import Room
        if not room:
            raise ValueError("room is required")
        if not isinstance(room, Room):
            raise ValueError("room must be an instance of Room")
        if room not in self.__rooms:
            self.__rooms.append(room)
            room.hotel = self

    def remove_room(self, room: Room):
        if not room:
            raise ValueError("room is required")
        if not isinstance(room, Room):
            raise ValueError("room must be an instance of Room")
        if room in self.__rooms:
            self.__rooms.remove(room)
            room.hotel = None


    @property
    def room_type(self) -> list[RoomType]:
        return self.__room_type

    def add_room_type(self, room_type: RoomType) -> None:
        if not room_type:
            raise ValueError("room_type is required")
        if not isinstance(room_type, RoomType):
            raise ValueError("room_type must be an instance of RoomType")
        if room_type not in self.__room_type:
            self.__room_type.append(room_type)
            room_type.hotel = self

    def remove_room_type(self, room_type : RoomType) -> None:
        from model.room_type import RoomType
        if not room_type:
            raise ValueError("room_type is required")
        if not isinstance(room_type, RoomType):
            raise ValueError("room_type must be an instance of RoomType")
        if room_type in self.__room_type:
            self.__room_type.remove(room_type)
            room_type.hotel = None

