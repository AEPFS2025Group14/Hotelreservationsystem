import pandas as pd
from datetime import date, datetime

import data_access
from data_access.base_data_access import BaseDataAccess
from data_access.guest_data_access import GuestDataAccess
from data_access.room_data_access import RoomDataAccess
import model


class BookingDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None) -> None:
        super().__init__(db_path)
        self._guest_da = data_access.GuestDataAccess(db_path)
        self._room_da = data_access.RoomDataAccess(db_path)

    def create_new_booking(
            self,
            check_in_date: date,
            check_out_date: date,
            is_cancelled: bool,
            total_amount: float,
            guest: model.Guest,
            room: model.Room
    ) -> model.Booking:
        print("DEBUG: is_cancelled type/value", type(is_cancelled), is_cancelled)

        if check_in_date is None:
            raise ValueError("check_in_date is required")
        if check_out_date is None:
            raise ValueError("check_out_date is required")
        if check_in_date >= check_out_date:
            raise ValueError("check_in_date must be before check_out_date")
        if guest is None:
            raise ValueError("guest is required")
        if room is None:
            raise ValueError("room is required")
        if total_amount is None:
            total_amount = 0.0

        if not self.is_room_available(room.room_id, check_in_date, check_out_date):
            raise Exception(f"Zimmer {room.room_id} ist im angegebenen Zeitraum nicht verfügbar.")

        sql = """
        INSERT INTO Booking (guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        params = (guest.guest_id, room.room_id, check_in_date, check_out_date, is_cancelled, total_amount)
        last_row_id, row_count = self.execute(sql, params)

        print("DEBUG: Returning Booking with is_cancelled", is_cancelled)
        return model.Booking(
            booking_id=last_row_id,
            guest=guest,
            room=room,
            check_in_date=check_in_date,
            check_out_date=check_out_date,
            is_cancelled=is_cancelled,
            total_amount=total_amount
        )


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



    def read_booking_by_id(self, booking_id: int) -> model.Booking | None:
        sql = """
        SELECT booking_id, guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount
        FROM Booking WHERE booking_id = ?
        """
        result = self.fetchone(sql, (booking_id,))
        if result:
            booking_id, guest_id, room_id, check_in, check_out, cancelled, total = result

            total = total if total is not None else 0.0
            # ✅ Datumsfelder prüfen und konvertieren
            if isinstance(check_in, str):
                check_in = datetime.strptime(check_in, "%Y-%m-%d").date()
            if isinstance(check_out, str):
                check_out = datetime.strptime(check_out, "%Y-%m-%d").date()

            # ✅ Zuordnungen laden
            guest = self._guest_da.read_guest_by_id(guest_id)
            room = self._room_da.get_room_by_id(room_id)

            return model.Booking(
                booking_id=booking_id,
                guest=guest,
                room=room,
                check_in_date=check_in,
                check_out_date=check_out,
                is_cancelled=bool(cancelled),
                total_amount=total
            )
        return None

    def read_all_bookings(self) -> list[model.Booking]:
        sql = """
        SELECT booking_id, guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount FROM Booking
        """
        rows = self.fetchall(sql)
        result = []

        for row in rows:
            booking_id, guest_id, room_id, check_in, check_out, cancelled, total = row

            total = total if total is not None else 0.0
            # Datum konvertieren, falls als String
            if isinstance(check_in, str):
                check_in = datetime.strptime(check_in, "%Y-%m-%d").date()
            if isinstance(check_out, str):
                check_out = datetime.strptime(check_out, "%Y-%m-%d").date()

            # Gast & Zimmer laden
            guest = self._guest_da.read_guest_by_id(guest_id)
            room = self._room_da.get_room_by_id(room_id)

            booking = model.Booking(
                booking_id=booking_id,
                guest=guest,
                room=room,
                check_in_date=check_in,
                check_out_date=check_out,
                is_cancelled=bool(cancelled),
                total_amount=total

            )

            result.append(booking)

        return result

    def read_all_bookings_as_df(self) -> pd.DataFrame:
        sql = "SELECT * FROM Booking"
        return pd.read_sql(sql, self._connect(), index_col='booking_id')

    def cancel_booking(self, booking: model.Booking) -> model.Booking:
        if booking is None:
            raise ValueError(" cancel_booking wurde mit None aufgerufen – ungültige Buchung.")

        sql = """
        UPDATE Booking SET is_cancelled = 1, total_amount = 0 WHERE booking_id = ?
        """
        self.execute(sql, (booking.booking_id,))

        booking.is_cancelled = True
        booking.total_amount = 0.0

        return booking

    def update_booking(self, booking: model.Booking) -> None:
        sql = """
        UPDATE Booking SET guest_id = ?, room_id = ?, check_in_date = ?, check_out_date = ?, is_cancelled = ?, total_amount = ?
        WHERE booking_id = ? 
        """

        params = tuple([booking.guest.guest_id, booking.room.room_id, booking.check_in_date, booking.check_out_date,])

    def delete_booking(self, booking: model.Booking) -> None:
        self.execute("DELETE FROM Booking WHERE booking_id = ?", (booking.booking_id,))

    def get_all_bookings(self) -> list[dict]:

        query = """
            SELECT 
                b.booking_id,
                b.check_in_date,
                b.check_out_date,
                b.is_cancelled,
                b.total_amount,
                r.room_number,
                h.name AS hotel_name,
                g.first_name || ' ' || g.last_name AS guest_name
            FROM Booking b
            JOIN Room r ON b.room_id = r.room_id
            JOIN Hotel h ON r.hotel_id = h.hotel_id
            JOIN Guest g ON b.guest_id = g.guest_id
            ORDER BY b.check_in_date DESC
        """
        results = self.fetchall(query)
        buchungen = []

        for row in results:
            (
                booking_id, check_in, check_out, is_cancelled,
                total, room_number, hotel_name, guest_name
            ) = row

            buchungen.append({
                "Buchungs-ID": booking_id,
                "Hotel": hotel_name,
                "Zimmer": room_number,
                "Gast": guest_name,
                "Check-in": check_in,
                "Check-out": check_out,
                "Storniert": bool(is_cancelled),
                "Gesamtbetrag (CHF)": total
            })

        return buchungen

    def get_booking_by_id(self, booking_id: int) -> model.Booking | None:
        sql = """
            SELECT booking_id, guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount
            FROM Booking
            WHERE booking_id = ?
        """
        row = self._fetchone(sql, (booking_id,))
        if row:
            guest = self._load_guest_by_id(row["guest_id"])
            room = self._load_room_by_id(row["room_id"])
            return model.Booking(
                booking_id=row["booking_id"],
                guest=guest,
                room=room,
                check_in_date=row["check_in_date"],
                check_out_date=row["check_out_date"],
                is_cancelled=bool(row["is_cancelled"]),
                total_amount=row["total_amount"]
            )
        return None

