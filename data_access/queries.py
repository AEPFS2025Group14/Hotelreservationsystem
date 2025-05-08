import sqlite3
import pandas as pd

DB_PATH = "database/hotel_reservation_sample.db"

def search_hotels_by_city(city_name):
    conn = sqlite3.connect(DB_PATH)
    query = """
    SELECT h.name, a.street, a.zip_code, a.city, h.stars
    FROM Hotel h
    JOIN Address a ON h.address_id = a.address_id
    WHERE a.city = ?
    """
    df = pd.read_sql_query(query, conn, params=(city_name,))
    conn.close()
    return df

import sqlite3
import pandas as pd

DB_PATH = "database/hotel_reservation_sample.db"

def search_hotels_by_city(city):
    conn = sqlite3.connect(DB_PATH)
    query = """
    SELECT h.hotel_id, h.name, h.stars, a.city, a.street, a.zip_code
    FROM Hotel h
    JOIN Address a ON h.address_id = a.address_id
    WHERE a.city = ?
    """
    df = pd.read_sql_query(query, conn, params=(city,))
    conn.close()
    return df

def get_available_rooms(hotel_id, check_in_date, check_out_date):
    conn = sqlite3.connect(DB_PATH)
    query = """
    SELECT r.room_id, r.room_number, rt.description, r.price_per_night
    FROM Room r
    JOIN Room_Type rt ON r.type_id = rt.type_id
    WHERE r.hotel_id = ?
    AND r.room_id NOT IN (
        SELECT b.room_id
        FROM Booking b
        WHERE NOT (
            b.check_out_date <= ? OR
            b.check_in_date >= ?
        )
    )
    """
    df = pd.read_sql_query(query, conn, params=(hotel_id, check_in_date, check_out_date))
    conn.close()
    return df

def book_room(guest_id, room_id, check_in_date, check_out_date):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT price_per_night FROM Room WHERE room_id = ?", (room_id,))
    price = cursor.fetchone()[0]
    nights = (pd.to_datetime(check_out_date) - pd.to_datetime(check_in_date)).days
    total = nights * price

    cursor.execute("""
    INSERT INTO Booking (guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount)
    VALUES (?, ?, ?, ?, 0, ?)
    """, (guest_id, room_id, check_in_date, check_out_date, total))
    conn.commit()
    conn.close()
    return total

def generate_invoice(booking_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT total_amount FROM Booking WHERE booking_id = ?", (booking_id,))
    total = cursor.fetchone()[0]

    cursor.execute("""
    INSERT INTO Invoice (booking_id, issue_date, total_amount)
    VALUES (?, DATE('now'), ?)
    """, (booking_id, total))
    conn.commit()
    conn.close()
    return total

def search_hotels_filtered(city, min_stars, guest_count, check_in, check_out):
    conn = sqlite3.connect(DB_PATH)
    query = """
    SELECT DISTINCT h.hotel_id, h.name, h.stars, a.city, a.street, a.zip_code
    FROM Hotel h
    JOIN Address a ON h.address_id = a.address_id
    JOIN Room r ON h.hotel_id = r.hotel_id
    JOIN Room_Type rt ON r.type_id = rt.type_id
    WHERE a.city = ?
      AND h.stars >= ?
      AND rt.max_guests >= ?
      AND r.room_id NOT IN (
          SELECT b.room_id
          FROM Booking b
          WHERE NOT (
              b.check_out_date <= ? OR
              b.check_in_date >= ?
          )
      )
    """
    df = pd.read_sql_query(query, conn, params=(city, min_stars, guest_count, check_in, check_out))
    conn.close()
    return df

def get_room_details(hotel_id, check_in, check_out):
    conn = sqlite3.connect(DB_PATH)
    query = """
    SELECT r.room_id, r.room_number, rt.description AS room_type, rt.max_guests,
           r.price_per_night, GROUP_CONCAT(f.facility_name, ', ') AS facilities
    FROM Room r
    JOIN Room_Type rt ON r.type_id = rt.type_id
    LEFT JOIN Room_Facilities rf ON r.room_id = rf.room_id
    LEFT JOIN Facilities f ON rf.facility_id = f.facility_id
    WHERE r.hotel_id = ?
      AND r.room_id NOT IN (
          SELECT b.room_id
          FROM Booking b
          WHERE NOT (
              b.check_out_date <= ? OR
              b.check_in_date >= ?
          )
      )
    GROUP BY r.room_id
    ORDER BY r.price_per_night ASC
    """
    df = pd.read_sql_query(query, conn, params=(hotel_id, check_in, check_out))
    conn.close()
    return df

def add_hotel(name, stars, address_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Hotel (name, stars, address_id)
        VALUES (?, ?, ?)
    """, (name, stars, address_id))
    conn.commit()
    conn.close()

def update_hotel(hotel_id, name, stars, address_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Hotel
        SET name = ?, stars = ?, address_id = ?
        WHERE hotel_id = ?
    """, (name, stars, address_id, hotel_id))
    conn.commit()
    conn.close()

def delete_hotel(hotel_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Hotel WHERE hotel_id = ?", (hotel_id,))
    conn.commit()
    conn.close()

def cancel_booking(booking_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Setze Buchung auf "storniert"
    cursor.execute("""
        UPDATE Booking
        SET is_cancelled = 1,
            total_amount = 0
        WHERE booking_id = ?
    """, (booking_id,))

    # Falls Rechnung existiert → auch auf 0 CHF setzen
    cursor.execute("""
        UPDATE Invoice
        SET total_amount = 0
        WHERE booking_id = ?
    """, (booking_id,))

    conn.commit()
    conn.close()

def get_total_revenue_by_period(start_date, end_date):
    conn = sqlite3.connect(DB_PATH)
    query = """
    SELECT SUM(total_amount) AS revenue
    FROM Booking
    WHERE is_cancelled = 0
      AND check_in_date >= ?
      AND check_out_date <= ?
    """
    df = pd.read_sql_query(query, conn, params=(start_date, end_date))
    conn.close()
    return df

def add_review(hotel_id, guest_id, rating, comment):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO Review (hotel_id, guest_id, rating, comment)
        VALUES (?, ?, ?, ?)
    """, (hotel_id, guest_id, rating, comment))

    conn.commit()
    conn.close()

