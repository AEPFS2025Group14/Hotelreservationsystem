import pandas as pd
import model
from data_access.base_data_access import BaseDataAccess


class BookingDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_new_booking(self, guest: model.Guest, room: model.Room, check_in: str, check_out: str) -> model.Booking:
        sql = """
        INSERT INTO Booking (guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount)
        VALUES (?, ?, ?, ?, 0, NULL)
        """
        params = (guest.guest_id, room.room_id, check_in, check_out)
        last_row_id, _ = self.execute(sql, params)
        return model.Booking(last_row_id, guest, room, check_in, check_out, False, None)

    def read_booking_by_id(self, booking_id: int) -> model.Booking | None:
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
        params = (
            booking.guest_id,
            booking.room_id,
            booking.check_in,
            booking.check_out,
            int(booking.is_cancelled),
            booking.total_amount,
            booking.booking_id
        )
        self.execute(sql, params)

    def delete_booking(self, booking: model.Booking) -> None:
        self.execute("DELETE FROM Booking WHERE booking_id = ?", (booking.booking_id,))
