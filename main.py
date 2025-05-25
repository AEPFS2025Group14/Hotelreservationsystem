import sqlite3

DB_PATH = "database/hotel_reservation_sample.db"  # anpassen falls dein Pfad anders ist

def create_review_table():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Review (
            review_id INTEGER PRIMARY KEY AUTOINCREMENT,
            hotel_id INTEGER NOT NULL,
            guest_id INTEGER NOT NULL,
            rating INTEGER CHECK(rating BETWEEN 1 AND 5),
            comment TEXT,
            FOREIGN KEY (hotel_id) REFERENCES Hotel(hotel_id),
            FOREIGN KEY (guest_id) REFERENCES Guest(guest_id)
        )
    """)
    conn.commit()
    conn.close()

create_review_table()

from data_access.queries import (
    search_hotels_by_city,
    get_available_rooms,
    book_room,
    generate_invoice,
    add_hotel,
    update_hotel,
    delete_hotel,
    cancel_booking,
    search_hotels_filtered,
    get_room_details
)

from data_access.queries import (
    search_hotels_by_city,
    get_available_rooms,
    book_room,
    generate_invoice
)

def main():
    print("HOTEL RESERVIERUNGSSYSTEM")
    print("1. Hotels in einer Stadt anzeigen")
    print("2. Verfügbare Zimmer anzeigen")
    print("3. Zimmer buchen")
    print("4. Rechnung erstellen")

    choice = input("Auswahl (1–4): ")

    if choice == "1":
        city = input("Stadt: ")
        print(search_hotels_by_city(city))

    elif choice == "2":
        hotel_id = int(input("Hotel ID: "))
        check_in: str = input("Check-In Datum (YYYY-MM-DD): ")
        check_out = input("Check-Out Datum (YYYY-MM-DD): ")
        print(get_available_rooms(hotel_id, check_in, check_out))

    elif choice == "3":
        guest_id = int(input("Gast-ID: "))
        room_id = int(input("Zimmer-ID: "))
        check_in = input("Check-In Datum (YYYY-MM-DD): ")
        check_out = input("Check-Out Datum (YYYY-MM-DD): ")
        total = book_room(guest_id, room_id, check_in, check_out)
        print(f"Buchung erfolgreich. Gesamtbetrag: {total:.2f} CHF")

    elif choice == "4":
        booking_id = int(input("Buchungs-ID: "))
        total = generate_invoice(booking_id)
        print(f"Rechnung erstellt: Gesamtbetrag = {total:.2f} CHF")

    else:
        print("Ungültige Auswahl")

if __name__ == "__main__":
    main()

from data_access.queries import search_hotels_filtered

results = search_hotels_filtered("Zürich", 4, 2, "2025-07-10", "2025-07-15")
print(results)

from data_access.queries import get_room_details

rooms = get_room_details(1, "2025-07-10", "2025-07-15")
print(rooms)

# Neues Hotel hinzufügen
add_hotel("Testhotel Zürich", 4, 1)

# Hotel aktualisieren
def update_hotel(param, param1, param2, param3):
    pass


update_hotel(1, "Renoviertes Hotel Baur au Lac", 5, 1)

# Hotel löschen
delete_hotel(5)

booking_id = int(input("Buchungs-ID zum Stornieren: "))
cancel_booking(booking_id)
print("Buchung erfolgreich storniert.")

from utils.pdf_export import create_booking_confirmation

# Beispielwerte (diese solltest du dynamisch aus Buchung nehmen)
guest_name = "Max Muster"
hotel_name = "Hotel Zürich"
check_in = "2025-07-10"
check_out = "2025-07-15"
total = 900.00

create_booking_confirmation(guest_name, hotel_name, check_in, check_out, total)
print("PDF-Bestätigung wurde erstellt!")

def create_review_table():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Review (
            review_id INTEGER PRIMARY KEY AUTOINCREMENT,
            hotel_id INTEGER NOT NULL,
            guest_id INTEGER NOT NULL,
            rating INTEGER CHECK(rating BETWEEN 1 AND 5),
            comment TEXT,
            FOREIGN KEY (hotel_id) REFERENCES Hotel(hotel_id),
            FOREIGN KEY (guest_id) REFERENCES Guest(guest_id)
        )
    """)
    conn.commit()
    conn.close()

