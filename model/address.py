from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .hotel import Hotel
    from .guest import Guest






class Address:
    def __init__(self, address_id: int, street:str, city:str, zip_code:str, hotel : Hotel = None, guest :Guest = None):
        from model import Hotel
        from model import Guest

        if not address_id:
            raise ValueError("address_id is required")
        if not isinstance(address_id, int):
            raise ValueError("address_id must be an integer")
        if not street:
            raise ValueError("stress is required")
        if not isinstance(street, str):
            raise ValueError("street must be an string")
        if not city:
            raise ValueError("city is required")
        if not isinstance(city, str):
            raise ValueError("city must be a string")
        if not zip_code:
            raise ValueError("zip code is required")
        if not isinstance(zip_code, str):
            raise ValueError("zip code must be a string")

        if hotel is not None and not isinstance(hotel, Hotel):
            raise ValueError("hotel must be an instance of Hotel")
        if guest is not None and not isinstance(guest, Guest):
            raise ValueError("guest must be an instance of Guest")

        self.__address_id: int = address_id
        self.__street: str = street
        self.__city: str = city
        self.__zip_code: str = zip_code
        if hotel is not None:
            hotel.add_address(self)
        self.__guest : Guest = []



    def __repr__(self):
        return (f"Address(id={self.__address_id!r}, "
                f"street={self.__street!r}, city={self.__city!r}, zip_code={self.__zip_code!r})")

    @property
    def address_id(self) -> int:
        return self.__address_id

    @property
    def street(self) -> str:
        return self.__street

    @street.setter
    def street(self, street:str) -> None:
        self.__street = street
        if not street:
            raise ValueError("street is required")
        if not isinstance(street, str):
            raise ValueError("street must be an string")
        self.__street = street

    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, city:str) -> None:
        self.__city = city
        if not city:
            raise ValueError("city is required")
        if not isinstance(city, str):
            raise ValueError("city must be an string")
        self.__city = city

    @property
    def zip_code(self) -> str:
        return self.__zip_code
    @zip_code.setter
    def zip_code(self, zip_code:str) -> None:
        self.__zip_code = zip_code
        if not zip_code:
            raise ValueError("zip code is required")
        if not isinstance(zip_code, str):
            raise ValueError("zip code must be an string")
        self.__zip_code = zip_code


    @property
    def hotel(self) -> Hotel:
        return self.__hotel

    @hotel.setter
    def hotel(self, hotel:Hotel) -> None:
        """Sets the hotel for this address
        Also adds this address to the hotels address if it isn't already present.
        If the address already belonged to a different hotel, it removes itself from that hotel.
        Passing 'None' as the Hotel clears the current address"""
        from .hotel import Hotel
        if hotel is not None and not isinstance(hotel, Hotel):
            raise TypeError("hotel must be an instance of Hotel")

        if self.__hotel is not hotel:
            if self.__hotel is not None:
                self.__hotel.remove_address(self)
            self.__hotel = hotel

            if hotel is not None and self not in hotel.address:
                hotel.add_address(self)


    @property
    def guest(self) -> list[Guest]:
        return self.__guest

    def add_guest(self, guest: Guest):
        from .guest import Guest
        if not isinstance(guest, Guest):
            raise ValueError("guest must be an instance of Guest")
        if guest not in self.__guests:
            self.__guests.append(guest)
            if guest.address is not self:
                guest.address = self  # sorgt für Konsistenz

    def remove_guest(self, guest: Guest):
        if guest in self.__guests:
            self.__guests.remove(guest)
            if guest.address is self:
                guest.address = None