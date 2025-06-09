from __future__ import annotations
from typing import TYPE_CHECKING
from datetime import date, datetime

import model
from model.invoice import Invoice

if TYPE_CHECKING:
    from .guest import Guest
    from .room import Room
    from model.guest import Guest
    from model.invoice import Invoice




class Booking:
    def __init__(self, booking_id:int, check_in_date: date,check_out_date:date, is_cancelled:bool, total_amount:float, guest: Guest = None, room: Room = None):

        if booking_id is None:
            raise ValueError("booking_id is required")
        if not isinstance(booking_id, int):
            raise ValueError("booking_id must be an integer")
        if not check_in_date:
            raise ValueError("check_in_date is required")
        if not isinstance(check_in_date, date):
            raise ValueError("check_in_date must be an date")
        if not check_out_date:
            raise ValueError("check_out_date is required")
        if not isinstance(check_out_date, date):
            raise ValueError("check_out_date must be an date")
        if is_cancelled is None:
            raise ValueError("is_cancelled is required")
        if not isinstance(is_cancelled, bool):
            raise ValueError("is_cancelled must be an boolean")
        if total_amount is None:
            raise ValueError("total_amount is required")
        if not isinstance(total_amount, float):
            raise ValueError("total_amount must be a float")

        self.__booking_id : int = booking_id
        self.__check_in_date : date = check_in_date
        self.__check_out_date : date = check_out_date
        self.__is_cancelled : bool = is_cancelled
        self.__total_amount : float = total_amount
        self.__guest = guest
        self.__room: Room = room
        self.__invoice : list[Invoice] = []




        if guest is not None:
            guest.add_booking(self)
        if room is not None:
            room.add_booking(self)




    def __repr__(self):
        return (f"Booking={self.__booking_id!r}, check_in_date={self.__check_in_date!r}, "
        f"check_out_date={self.__check_out_date!r}, is_cancelled={self.__is_cancelled!r}, "
        f"total_amount={self.__total_amount!r}, guest={self.__guest!r}, room={self.__room!r}")




    @property
    def booking_id(self) -> int:
        return self.__booking_id

    @property
    def check_in_date(self) -> date:
        return self.__check_in_date

    @check_in_date.setter
    def check_in_date(self, check_in_date) -> None:
        if not check_in_date:
            raise ValueError("check_in_date is required")
        if not isinstance(check_in_date, date):
            raise ValueError("check_in_date must be an date")
        self.__check_in_date = check_in_date

    @property
    def check_out_date(self) -> date:
        return self.__check_out_date

    @check_out_date.setter
    def check_out_date(self, check_out_date: date) -> None:
        if not check_out_date:
            raise ValueError("check_out_date is required")
        if not isinstance(check_out_date, date):
            raise ValueError("check_out_date must be an date")
        self.__check_out_date = check_out_date

    @property
    def is_cancelled(self) -> bool:
        return self.__is_cancelled

    @is_cancelled.setter
    def is_cancelled(self, is_cancelled:bool) -> None:
        if not is_cancelled:
            raise ValueError("is_cancelled is required")
        if not isinstance(is_cancelled, bool):
            raise ValueError("is_cancelled must be an boolean")
        self.__is_cancelled = is_cancelled

    @property
    def total_amount(self) -> float:
        return self.__total_amount

    @total_amount.setter
    def total_amount(self, total_amount: float) -> None:
        if total_amount is None:
            raise ValueError("total_amount is required")
        if not isinstance(total_amount, float):
            raise ValueError("total_amount must be a float")
        self.__total_amount = total_amount


    @property
    def guest(self) -> model.Guest | None:
        return self.__guest

    def guest(self, guest: Guest | None) -> None:
        if guest is not None and not isinstance(guest, Guest):
            raise ValueError("guest must be a Guest or None")

        if self.__guest is not None and self.__guest is not guest:
            self.__guest.remove_booking(self)

        self.__guest = guest

        if guest is not None and self not in guest.bookings:
            guest.add_booking(self)


    @property
    def room(self) -> Room:
        return self.__room

    def add_room(self, room: Room) -> None:
        if not isinstance(room, Room):
            raise ValueError("room must be a Room")
        self.__room = room
        room.add_booking(self)

    def remove_room(self, room: Room) -> None:
        from model import Room
        if not room:
            raise ValueError("room is required")
        if not isinstance(room, Room):
            raise ValueError("room must be a Room")
        if room in self.__room:
            self.__room.remove(room)
            room.booking = None

    @property
    def invoice(self) -> list[Invoice]:
        return self.__invoice.copy()


    def add_invoice(self, invoice: Invoice) -> None:
        from model import Invoice

        if not invoice:
            raise ValueError("invoice is required")
        if not isinstance(invoice, Invoice):
            raise ValueError("invoice must be an Invoice")
        if invoice not in self.__invoice:
            self.__invoice.append(invoice)
            invoice.booking = self

    def remove_invoice(self, invoice: Invoice) -> None:
        from model import Invoice

        if not invoice:
            raise ValueError("invoice is required")
        if not isinstance(invoice, Invoice):
            raise ValueError("invoice must be an Invoice")
        if invoice in self.__invoice:
            self.__invoice.remove(invoice)
            invoice.booking = None

