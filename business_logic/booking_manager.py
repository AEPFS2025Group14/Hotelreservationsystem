import os
import pandas as pd

import model
import data_access


class BookingManager:
    def __init__(self):
        self.__booking_da = data_access.BookingDataAccess()

    def create_booking(self, guest: model.Guest, room: model.Room, check_in: str, check_out: str) -> model.Booking:
        return self.__booking_da.create_new_booking(guest, room, check_in, check_out)

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
