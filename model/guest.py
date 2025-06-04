from __future__ import annotations
from typing import TYPE_CHECKING

import model

if TYPE_CHECKING:
    from model import Address, Booking
    from model.booking import Booking



class Guest:
    def __init__(self, guest_id: int, last_name: str, first_name: str, email: str, address: Address = None):

        if not guest_id:
            raise ValueError("Guest ID is required")
        if not isinstance(guest_id, int):
            raise ValueError("Guest ID must be an integer")
        if not last_name:
            raise ValueError("Last name is required")
        if not isinstance(last_name, str):
            raise ValueError("Last name must be an string")
        if not first_name:
            raise ValueError("First name is required")
        if not isinstance(first_name, str):
            raise ValueError("First name must be an string")
        if not email:
            raise ValueError("Email is required")
        if not isinstance(email, str):
            raise ValueError("Email must be an string")


        self.__guest_id : int = guest_id
        self.__last_name : str = last_name
        self.__first_name : str = first_name
        self.__email : str = email
        self.__booking: list[Booking] = []




    def __repr__(self):
        return (f"Guest(id={self.__guest_id!r}, last_name={self.__last_name!r}"
                f",first_name={self.__first_name!r}, email={self.__email!r})")

    @property
    def guest_id(self) -> int:
        return self.__guest_id

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name : str) -> None:
        if not last_name:
            raise ValueError("Last name is required")
        if not isinstance(last_name, str):
            raise ValueError("Last name must be an string")
        self.__last_name = last_name

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name: str) -> None:
        if not first_name:
            raise ValueError("First name is required")
        if not isinstance(first_name, str):
            raise ValueError("First name must be an string")
        self.__first_name = first_name

    @property
    def email(self) -> str :
        return self.__email

    @email.setter
    def email(self, email: str) -> None:
        if not email:
            raise ValueError("Email is required")
        if isinstance(email, str):
            raise ValueError("Email must be an string")
        self.__email = email

    @property
    def booking(self) -> list[Booking]:
        return self.__booking.copy()

    def add_booking(self, booking: model.Booking) -> None:
        if booking not in self.__booking:
            self.__booking.append(booking)
            if booking.guest is not self:
                booking.guest = self

    def remove_booking(self, booking: model.Booking) -> None:
        if self.__booking == booking:
            self.__booking = None
            booking.guest = None


