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


# 5. Als Gast möchte ich nach meinem Aufenthalt eine Rechnung erhalten, damit ich einen Zahlungsnachweis habe. Hint: Fügt einen Eintrag in der «Invoice» Tabelle hinzu.

def get_booking_by_id(booking_id: int, cursor=None):
    cursor.execute("""
        SELECT booking_id, is_cancelled, total_amount FROM Booking
        WHERE booking_id = ?
    """, (booking_id,))
    row = cursor.fetchone()
    if row:
        # Rückgabe eines simplen Objekts oder namedtuple
        return type('Booking', (object,), {
            'booking_id': row[0],
            'is_cancelled': bool(row[1]),
            'total_amount': row[2]
        })()
    return None

#6. Als Gast möchte ich meine Buchung stornieren, damit ich nicht belastet werde, wenn ich das Zimmer nicht mehr benötige. Hint: Sorgt für die entsprechende Invoice.

def cancel_booking(booking_id: int):
    cursor.execute("""
        UPDATE Booking
        SET is_cancelled = 1, total_amount = 0.00
        WHERE booking_id = ?
    """, (booking_id,))
    conn.commit()
