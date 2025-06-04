import pandas as pd
from datetime import date, datetime
from data_access.base_data_access import BaseDataAccess
import model


class BookingDataAccess(BaseDataAccess):
    def __init__(self, db_path: str) -> None:
        super().__init__(db_path)

    def create_new_booking(self,check_in_date: date,check_out_date:date, is_cancelled:bool, total_amount:float, guest: model.Guest, room: model.Room) -> model.Booking:
        print("DEBUG: is_cancelled type/value", type(is_cancelled), is_cancelled)
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

        if not self.is_room_available(room.room_id, check_in_date, check_out_date):
            raise Exception(f"Zimmer {room.room_id} ist im angegebenen Zeitraum nicht verfügbar.")


        sql = """
        INSERT INTO Booking (guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        params = (guest.guest_id, room.room_id, check_in_date, check_out_date, is_cancelled, total_amount)
        last_row_id, row_count = self.execute(sql, params)

        print("DEBUG: Returning Booking with is_cancelled", is_cancelled)
        return model.Booking(booking_id=last_row_id, guest=guest,room= room,check_in_date=check_in_date,check_out_date=check_out_date,is_cancelled=is_cancelled, total_amount = total_amount)


    def is_room_available(self, room_id: int, check_in_date: date, check_out_date: date) -> bool:
        sql = """
        SELECT COUNT(*) FROM Booking
        WHERE room_id = ? AND is_cancelled = 0 AND (
            (check_in_date <= ? AND check_out_date > ?) OR
            (check_in_date < ? AND check_out_date >= ?) OR
            (check_in_date >= ? AND check_out_date <= ?)
        )
        """
        params = (
            room_id,
            check_in_date, check_in_date,
            check_out_date, check_out_date,
            check_in_date, check_out_date
        )
        count_row = self.fetchone(sql, params)
        count = count_row[0] if count_row else 0
        return count == 0

    def read_booking_by_id(self, booking_id: int) -> model.Booking :
        sql = """
        SELECT booking_id, guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount
        FROM Booking WHERE booking_id = ?
        """
        params = (booking_id,)
        result = self.fetchone(sql, params)
        if result:
            booking_id, guest_id, room_id, check_in, check_out, cancelled, total = result
            return model.Booking(booking_id, guest_id, room_id, check_in, check_out, bool(cancelled), total)
        return None

    def read_all_bookings(self) -> list[model.Booking]:
        sql = """
        SELECT booking_id, guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount FROM Booking
        """
        rows = self.fetchall(sql)
        return [model.Booking(*row) for row in rows]

    def read_all_bookings_as_df(self) -> pd.DataFrame:
        sql = "SELECT * FROM Booking"
        return pd.read_sql(sql, self._connect(), index_col='booking_id')

    def cancel_booking(self, booking: model.Booking) -> None:
        sql = """
        UPDATE Booking SET is_cancelled = 1, total_amount = 0 WHERE booking_id = ?
        """
        self.execute(sql, (booking.booking_id,))

    def update_booking(self, booking: model.Booking) -> None:
        sql = """
        UPDATE Booking SET guest_id = ?, room_id = ?, check_in_date = ?, check_out_date = ?, is_cancelled = ?, total_amount = ?
        WHERE booking_id = ? 
        """

        params = tuple([booking.guest.guest_id, booking.room.room_id, booking.check_in_date, booking.check_out_date,])

    def delete_booking(self, booking: model.Booking) -> None:
        self.execute("DELETE FROM Booking WHERE booking_id = ?", (booking.booking_id,))
