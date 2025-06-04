import os
import pandas as pd
import model
from datetime import date, datetime
import data_access
from model import Guest, Room


class BookingManager:
    def __init__(self) -> None:
        self.__booking_da = data_access.BookingDataAccess()

    def create_new_booking(self, check_in_date: date, check_out_date: date, is_cancelled: bool, total_amount: float, guest: model.Guest, room: model.Room) -> model.Booking:
            return self.__booking_da.create_new_booking(check_in_date=check_in_date, check_out_date=check_out_date,
                                                        is_cancelled=is_cancelled, total_amount=total_amount, guest=guest, room=room)

    def is_room_available(self, room_id: int, check_in_date: date, check_out_date: date) -> bool:
        return self.__booking_da.is_room_available(room_id=room_id, check_in_date=check_in_date, check_out_date=check_out_date)

    def read_booking(self, booking_id: int) -> model.Booking:
        return self.__booking_da.read_booking_by_id(booking_id)

    def read_all_bookings(self) -> list[model.Booking]:
        return self.__booking_da.read_all_bookings()

    def read_all_bookings_as_df(self) -> pd.DataFrame:
        return self.__booking_da.read_all_bookings_as_df()

    def cancel_booking(self, booking: model.Booking) -> None:
        self.__booking_da.cancel_booking(booking)

    def update_booking(self, booking: model.Booking) -> None:
        self.__booking_da.update_booking(booking)

    def delete_booking(self, booking: model.Booking) -> None:
        self.__booking_da.delete_booking(booking)
