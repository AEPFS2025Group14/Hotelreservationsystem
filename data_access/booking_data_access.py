import pandas as pd
import model
from datetime import date, datetime
from data_access.base_data_access import BaseDataAccess
from model import Guest, Room, booking


class BookingDataAccess(BaseDataAccess):
    def __init__(self, db_path: str) -> None:
        super().__init__(db_path)

    def create_new_booking(self,check_in_date: date,check_out_date:date, is_cancelled:bool, total_amount:float, guest: Guest, room: Room) -> model.booking:
        if check_in_date is None:
            raise ValueError("check_in_date is required")
        if check_out_date is None:
            raise ValueError("check_out_date is required")
        if check_in_date >= check_out_date:
            raise ValueError("check_in_date must be greater than check_out_date")
        if is_cancelled is None:
            raise ValueError("is_cancelled is required")
        if total_amount is None:
            raise ValueError("total_amount is required")
        if guest is None:
            raise ValueError("guest is required")
        if room is None:
            raise ValueError("room is required")

        sql = """
        INSERT INTO Booking (guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount)
        VALUES (?, ?, ?, ?, 0, NULL)
        """
        params = (guest.guest_id, room.room_id, check_in_date, check_out_date, is_cancelled, total_amount)
        last_row_id, row_count = self.execute(sql, params)
        return model.booking(last_row_id, guest, room, check_in_date, check_out_date, total_amount, is_cancelled)

    def read_booking_by_id(self, booking_id: int) -> model.booking :
        sql = """
        SELECT booking_id, guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount
        FROM Booking WHERE booking_id = ?
        """
        params = (booking_id,)
        result = self.fetchone(sql, params)
        if result:
            booking_id, guest_id, room_id, check_in, check_out, cancelled, total = result
            return model.booking(booking_id, guest_id, room_id, check_in, check_out, bool(cancelled), total)
        return None

    def read_all_bookings(self) -> list[model.booking]:
        sql = """
        SELECT booking_id, guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount FROM Booking
        """
        rows = self.fetchall(sql)
        return [model.booking(*row) for row in rows]

    def read_all_bookings_as_df(self) -> pd.DataFrame:
        sql = "SELECT * FROM Booking"
        return pd.read_sql(sql, self._connect(), index_col='booking_id')

    def cancel_booking(self, booking: model.booking) -> None:
        sql = """
        UPDATE Booking SET is_cancelled = 1, total_amount = 0 WHERE booking_id = ?
        """
        self.execute(sql, (booking.booking_id,))

    def update_booking(self, booking: model.booking) -> None:
        sql = """
        UPDATE Booking SET guest_id = ?, room_id = ?, check_in_date = ?, check_out_date = ?, is_cancelled = ?, total_amount = ?
        WHERE booking_id = ? 
        """

        params = tuple([booking.guest_id, booking.room_id, booking.check_in_date, booking.check_out_date,])

    def delete_booking(self, booking: model.booking) -> None:
        self.execute("DELETE FROM Booking WHERE booking_id = ?", (booking.booking_id,))
