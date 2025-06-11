from __future__ import annotations
from typing import TYPE_CHECKING

import model

if TYPE_CHECKING:
    from .hotel import Hotel
    from .room_type import RoomType
    from .facilities import Facility
    from model.booking import Booking



class Room:
    def __init__(self, room_id:int, room_number: str, room_type:RoomType, price_per_night : float, hotel: Hotel = None):
        from .room_type import RoomType
        if not room_id:
            raise ValueError("Room ID is required")
        if not isinstance(room_id, int):
            raise ValueError("Room ID must be an integer")
        if not room_number:
            raise ValueError("Room number is required")
        if not isinstance(room_number, str):
            raise ValueError("Room number must be an string")
        if not room_type:
            raise ValueError("Room type is required")
        if not isinstance(room_type, RoomType):
            raise ValueError("Room type must be a RoomType")
        if hotel is not None and not isinstance(hotel, Hotel):
            raise ValueError("Hotel must be an instance of Hotel")



        self.__room_id : int = room_id
        self.__room_number : str = room_number
        self.__room_type : RoomType = room_type
        self.__facility : list[Facility] = []
        self.__price_per_night : float = price_per_night
        self.__hotel : Hotel = hotel
        self.__bookings: list[Booking] = []

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
        if not isinstance(room_number, int):
            raise ValueError("Room ID must be an integer")
        if not room_number:
            raise ValueError("Room number is required")
        self.__room_number = room_number

    @property
    def room_type(self) -> RoomType:
        return self.__room_type
    @room_type.setter
    def room_type(self, room_type: RoomType) -> None:
        if not room_type:
            raise ValueError("Room type is required")
        if not isinstance(room_type, RoomType):
            raise ValueError("Room type must be a RoomType")
        self.__room_type = room_type

    @property
    def facility(self) -> list[Facility]:
        return self.__facility

    def add_facility(self, facility: Facility) -> None:
        from model import Facility
        if not facility:
            raise ValueError("Facility is required")
        if not isinstance(facility, Facility):
            raise ValueError("Facility must be an instance of Facility")
        if facility not in self.__facility:
            self.__facility.append(facility)
            facility.__room = self

    def remove_facility(self, facility: Facility) -> None:
        from model import Facility
        if not facility:
            raise ValueError("Facility is required")
        if not isinstance(facility, Facility):
            raise ValueError("Facility must be an instance of Facility")
        if facility in self.__facility:
            self.__facility.remove(facility)
            facility.room = None

    #def get_total_price(self, nights: int) -> float:
     #   return self.nights

    @property
    def hotel(self) -> Hotel:
        return self.__hotel

    @hotel.setter
    def hotel(self, hotel: Hotel) -> None:
        from .hotel import Hotel
        if hotel is not None and not isinstance(hotel, Hotel):
            raise ValueError("Hotel must be an instance of Hotel")

        if self.__hotel is not hotel:
            if self.__hotel is not None:
                self.__hotel.remove_room(self)
            self.__hotel = hotel

            if hotel is not None and self not in hotel.rooms:
                hotel.add_room(self)


    @property
    def price_per_night(self) -> float:
        return self.__price_per_night

    @price_per_night.setter
    def price_per_night(self, price_per_night: float) -> None:
        if not isinstance(price_per_night, float):
            raise ValueError("Price per night must be a float")
        self.__price_per_night = price_per_night


    @property
    def bookings(self) -> list[model.Booking]:
        return self.__booking

    def add_booking(self, booking: model.Booking) -> None:
        if booking is None:
            raise ValueError("Booking is required")
        if not isinstance(booking, model.Booking):
            raise ValueError("Booking must be an instance of Booking")

        # Liste initialisieren, falls nicht vorhanden (failsafe)
        if not hasattr(self, '_booking') or self._booking is None:
            self._booking = []

        # Nur hinzufügen, wenn noch nicht enthalten
        if booking not in self._booking:
            self._booking.append(booking)
