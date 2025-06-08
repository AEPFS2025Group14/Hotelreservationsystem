
from __future__ import annotations
from typing import TYPE_CHECKING

from datetime import date

import model

if TYPE_CHECKING:
    from model.booking import Booking

class Invoice:
    def __init__(self, invoice_id :int, issue_date: date, total_amount:float, booking: Booking =None):
        if not invoice_id:
            raise ValueError("Invoice ID is required")
        if not isinstance(invoice_id, int):
            raise ValueError("Invoice ID is not an integer")
        if not issue_date:
            raise ValueError("Issue date is required")
        if not isinstance(issue_date, date):
            raise ValueError("Issue date is not a date")
        if not total_amount:
            raise ValueError("Total amount is required")
        if not isinstance(total_amount, float):
            raise ValueError("Total amount is not a float")

        self.__invoice_id : int = invoice_id
        self.__issue_date : date = issue_date
        self.__total_amount : float = total_amount
        self.__booking : Booking = None
        if booking is not None:
            booking.add_invoice(self)


    def __repr__(self):
        return (f"Invoice(id={self.__invoice_id!r}, issue_date={self.__issue_date!r},"
                f"total_amount={self.__total_amount!r}, booking={self.__booking!r})")

    @property
    def invoice_id(self) ->int:
        return self.__invoice_id

    @property
    def booking(self) -> Booking:
        return self.__booking

    @booking.setter
    def booking(self, booking : Booking) -> None:
        from booking import Booking
        if booking is None and not isinstance(booking, Booking):
            raise ValueError("Booking is required")
        if self.__booking is not booking:
            if self.__booking is not None:
                self.__boooking.remove_booking()
            self.booking = booking
            if booking is not None and self not in booking:
                booking.add_booking(self)


    @property
    def issue_date(self) ->date:
        return self.__issue_date

    @issue_date.setter
    def issue_date(self, issue_date : date) -> None:
        if not issue_date:
            raise ValueError("Issue date is required")
        if not isinstance(issue_date, date):
            raise ValueError("Issue date is not a date")
        self.__issue_date = issue_date

    @property
    def total_amount(self) ->float:
        return self.__total_amount
    @total_amount.setter
    def total_amount(self, total_amount : float) -> None:
        if not total_amount:
            raise ValueError("Total amount is required")
        if not isinstance(total_amount, float):
            raise ValueError("Total amount is not a float")
        self.__total_amount = total_amount

    @property
    def booking(self) -> model.Booking:
        return self.__booking

    @booking.setter
    def booking(self, booking: model.Booking) -> None:
        if booking is not None and not isinstance(booking, model.Booking):
            raise ValueError("booking must be a Booking instance or None")

        if self.__booking is not None:
            self.__booking.remove_invoice(self)

        self.__booking = booking

        if booking is not None and self not in booking.invoice:
            booking.add_invoice(self)
