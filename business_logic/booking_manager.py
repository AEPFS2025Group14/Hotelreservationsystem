import os
import pandas as pd
import model
from datetime import date, datetime
import data_access
from model import Guest, Room


class InvalidBookingException(Exception):
    pass


class AlreadyCancelledException(InvalidBookingException):
    pass

class BookingManager:
    def __init__(self) -> None:
        self.__booking_da = data_access.BookingDataAccess()
        self.__default_processing_fee_rate = 0.2

    def create_new_booking(self, check_in_date: date, check_out_date: date, is_cancelled: bool, total_amount: float, guest: model.Guest, room: model.Room) -> model.Booking:
        self.validate_booking_dates(check_in_date, check_out_date)
        return self.__booking_da.create_new_booking(check_in_date=check_in_date, check_out_date=check_out_date,
                                                        is_cancelled=is_cancelled, total_amount=total_amount, guest=guest, room=room)

    def is_room_available(self, room_id: int, check_in_date: date, check_out_date: date) -> bool:
        self.validate_booking_dates(check_in_date, check_out_date)
        return self.__booking_da.is_room_available(room_id=room_id, check_in_date=check_in_date, check_out_date=check_out_date)

    def read_booking(self, booking_id: int) -> model.Booking:

        return self.__booking_da.read_booking_by_id(booking_id)

    def read_all_bookings(self) -> list[model.Booking]:
        return self.__booking_da.read_all_bookings()

    def read_all_bookings_as_df(self) -> pd.DataFrame:
        return self.__booking_da.read_all_bookings_as_df()

    def update_booking(self, booking: model.Booking) -> None:
        if not booking:
            raise InvalidBookingException("None can not be updated")
        self.__booking_da.update_booking(booking)

    def delete_booking(self, booking: model.Booking) -> None:
        self.__booking_da.delete_booking(booking)

    def get_booking_by_id(self, booking_id: int) -> model.Booking:
        return self.__booking_da.read_booking_by_id(booking_id)

    def get_all_bookings(self) -> list[dict]:
        return self.__booking_da.get_all_bookings()

    def cancel_booking(self, booking: model.Booking) -> model.Booking:
        if not booking:
            raise InvalidBookingException("None can not be cancelled")

        if booking.is_cancelled:
            raise AlreadyCancelledException("Booking is already cancelled")

        today = date.today()
        if booking.check_in_date <= today:
            raise InvalidBookingException("Booking is in the past")

        booking.is_cancelled = True
        processing_fee = booking.total_amount * self.__default_processing_fee_rate
        booking.total_amount = processing_fee
        self.update_booking(booking)

        return booking

    def read_booking_by_id(self, booking_id: int) -> model.Booking | None:
       return  self.__booking_da.read_booking_by_id(booking_id)

    @staticmethod
    def validate_booking_dates(check_in_date: date, check_out_date: date) -> None:
        if check_in_date < date.today():
            raise ValueError("Check-in-Datum darf nicht in der Vergangenheit liegen.")
        if check_in_date >= check_out_date:
            raise ValueError("Check-out-Datum muss vor dem Check-out-Datum liegen.")