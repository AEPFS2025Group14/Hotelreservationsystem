

import model
import pandas as pd
from model.room_type import RoomType
from model.room import Room
from .base_data_access import BaseDataAccess
from .room_data_access import RoomDataAccess
from model.hotel import Hotel
from model.address import Address
from datetime import datetime, date


class HotelDataAccess(BaseDataAccess):
        def __init__(self, db_path: str = None):
            super().__init__(db_path)
            self.__room_da = RoomDataAccess()

        def search_hotels_by_city(self, city: str) -> list[model.Hotel]:

            query = """
                    SELECT h.hotel_id, h.name, h.stars, a.address_id, a.city, a.street, a.zip_code
                    FROM Hotel h
                    JOIN Address a ON h.address_id = a.address_id
                    WHERE UPPEr(a.city) = ?
                """
            results = self.fetchall(query, (city,))
            hotels = []
            for row in results:
                hotel_id, name, stars, address_id, city, street, zip_code = row
                address = Address(address_id, street, city, zip_code)
                hotel = Hotel(hotel_id, name, stars, address)
                hotels.append(hotel)
            return hotels

        def search_hotels_by_city_and_stars(self, city: str, stars: int) -> list[model.Hotel]:

                query = """ 
                    SELECT h.hotel_id, h.name, h.stars, a.address_id, a.city, a.street, a.zip_code
                    FROM Hotel h
                    JOIN Address a ON h.address_id = a.address_id
                    WHERE UPPER(a.city) = ? AND h.stars = ?
                    """


                results = self.fetchall(query, (city.upper(), stars))
                hotels = []
                for row in results:
                    hotel_id, name, stars, address_id, city, street, zip_code = row
                    address = Address(address_id, street, city, zip_code)
                    hotel = Hotel(hotel_id, name, stars, address)
                    hotels.append(hotel)
                return hotels

        def search_hotels_for_guests(self, city: str, stars: int, max_guests: int, room_typ_id=None, description = None) -> list[model.Hotel]:

                query = """
                    SELECT
                        h.hotel_id, h.name, h.stars, a.address_id, a.city, a.street, a.zip_code, 
                        rt.max_guests, rt.description, rt.type_id
                    FROM 
                        Hotel h
                    JOIN 
                        Address a ON h.address_id = a.address_id
                    JOIN 
                        Room r ON h.hotel_id = r.hotel_id
                    JOIN 
                        Room_Type rt ON r.type_id = rt.type_id
                    WHERE 
                        UPPER(a.city) = ? AND h.stars = ? AND rt.max_guests >= ?
                """
                results = self.fetchall(query, (city, stars, max_guests))
                hotels_by_id = {}

                for row in results:
                    hotel_id, name, stars, address_id, city, street, zip_code, max_guests_val, desc, room_type_id = row
                    room_type = RoomType(room_type_id, desc, max_guests_val)
                    address = Address(address_id, street, city, zip_code)

                    if hotel_id not in hotels_by_id:
                        hotel = Hotel(hotel_id, name, stars, address)
                        hotels_by_id[hotel_id] = hotel
                    else:
                        hotel = hotels_by_id[hotel_id]

                    hotel.add_room_type(room_type)

                return list(hotels_by_id.values())

        def search_hotel_Aufenthalt(self, city: str, check_in_date: str, check_out_date :str) -> list[model.Hotel]:
                sql = """
                    SELECT Room.room_id, Room.room_number, Room_Type.description, Room_Type.max_guests, Room_Type.type_id,
                           Hotel.name, Hotel.stars, Room.price_per_night, Hotel.hotel_id,
                           Address.address_id, Address.street, Address.city, Address.zip_code 
                    FROM Hotel 
                    JOIN Room ON Hotel.hotel_id = Room.hotel_id
                    JOIN Room_Type ON Room.type_id = Room_Type.type_id
                    JOIN Address ON Hotel.address_id = Address.address_id
                    WHERE UPPER(Address.city) = ?
                      AND Room.room_id NOT IN (
                        SELECT room_id
                        FROM Booking
                        WHERE is_cancelled = 0
                          AND NOT (
                                ? <= check_in_date OR 
                                ? >= check_out_date
                      )
                )
                """

                results = self.fetchall(sql, (city, check_out_date, check_in_date))
                hotels = []

                for row in results:
                    (
                        room_id, room_number, description, max_guests, room_type_id,
                        name, stars, price_per_night, hotel_id,
                        address_id, street, city, zip_code
                    ) = row

                    room_type = RoomType(room_type_id, description, max_guests)
                    room = Room(room_id, room_number, room_type, price_per_night)
                    address = Address(address_id, street, city, zip_code)
                    hotel = Hotel(hotel_id, name, stars, address)
                    hotel.add_room(room)
                    hotels.append(hotel)

                return hotels

        def search_hotel_combinated(self, city: str, check_in_date: str, check_out_date: str,
                                  min_stars: int = 0, max_guests: int = None) -> list[model.Hotel]:
                sql = """
                    SELECT Room.room_id, Room.room_number, Room_Type.description, Room_Type.max_guests, Room_Type.type_id,
                           Hotel.name, Hotel.stars, Room.price_per_night, Hotel.hotel_id,
                           Address.address_id, Address.street, Address.city, Address.zip_code 
                    FROM Hotel 
                    JOIN Room ON Hotel.hotel_id = Room.hotel_id
                    JOIN Room_Type ON Room.type_id = Room_Type.type_id
                    JOIN Address ON Hotel.address_id = Address.address_id
                    WHERE UPPER(Address.city) = ?
                      AND Hotel.stars >= ?
                      AND Room.room_id NOT IN (
                          SELECT room_id
                          FROM Booking
                          WHERE is_cancelled = 0
                            AND NOT (? <= check_in_date OR ? >= check_out_date)
                      )
                """

                params = [city, min_stars, check_in_date, check_out_date]

                if max_guests is not None:
                    sql += " AND Room_Type.max_guests >= ?"
                    params.append(max_guests)

                results = self.fetchall(sql, params)
                hotel_map = {}

                for row in results:
                    (
                            room_id, room_number, description, max_guests_row, room_type_id,
                            name, stars, price_per_night, hotel_id,
                            address_id, street, city_name, zip_code
                        ) = row

                    if max_guests_row < max_guests:
                        continue

                    room_type = RoomType(room_type_id, description, max_guests_row)
                    room = Room(room_id, room_number, room_type, price_per_night)
                    address = Address(address_id, street, city_name, zip_code)

                    if hotel_id not in hotel_map:
                        hotel = Hotel(hotel_id, name, stars, address)
                        hotel.add_room(room)
                        hotel_map[hotel_id] = hotel
                    else:
                        existing_hotel = hotel_map[hotel_id]
                        existing_room = existing_hotel.rooms[0]
                        if room.price_per_night < existing_room.price_per_night:
                            existing_hotel.rooms = [room]

                return list(hotel_map.values())

        def zeige_Information_pro_Hotel(self) -> list[model.Hotel]:

                query = """
                    SELECT Hotel.hotel_id, Hotel.name, Hotel.stars, Address.address_id, Address.street, Address.city, Address.zip_code
                    FROM Hotel 
                    JOIN Address ON Hotel.address_id = Address.address_id
                
                """

                results = self.fetchall(query)
                hotels = []

                for row in results:
                    hotel_id, name, stars, address_id, street, city, zip_code = row

                    address = Address(address_id, street, city, zip_code)
                    hotel = Hotel(hotel_id, name, stars, address)
                    hotels.append(hotel)

                return hotels

        def search_hotel_print_rooms(self, city: str, check_in_date: date = None, check_out_date: date = None,
                                     description=None, max_guests=None, room_type_id=None,
                                     address_id=None, zip_code=None, street=None, room_number=None) -> list[
            model.Hotel]:
            query = """
                SELECT 
                    Room.room_id, Room.room_number,
                    Room_Type.description, Room_Type.max_guests, Room_Type.type_id,
                    Room.price_per_night,
                    Hotel.name, Hotel.stars, Hotel.hotel_id,
                    Address.address_id, Address.street, Address.city, Address.zip_code
                FROM Hotel 
                JOIN Room ON Hotel.hotel_id = Room.hotel_id
                JOIN Room_Type ON Room.type_id = Room_Type.type_id
                JOIN Address ON Hotel.address_id = Address.address_id
                WHERE UPPER(Address.city) = ?
            """

            params = [city]

            if check_in_date and check_out_date:
                query += """
                    AND Room.room_id NOT IN (
                        SELECT room_id FROM Booking
                        SELECT room_id FROM Booking
                        WHERE NOT (
                            Booking.check_out_date <= ? OR
                            Booking.check_in_date >= ?
                        )
                    )
                """
                params.extend([check_in_date.isoformat(), check_out_date.isoformat()])

            results = self.fetchall(query, tuple(params))

            hotels_dict = {}

            for row in results:
                (
                    room_id, room_number, description, max_guests, room_type_id,
                    price_per_night,
                    name, stars, hotel_id,
                    address_id, street, city, zip_code
                ) = row

                room_type = RoomType(room_type_id, description, max_guests)
                room = Room(room_id, room_number, room_type, price_per_night)
                address = Address(address_id, street, city, zip_code)

                if hotel_id not in hotels_dict:
                    hotel = Hotel(hotel_id, name, stars, address)
                    hotels_dict[hotel_id] = hotel

                hotels_dict[hotel_id].add_room(room)

            return list(hotels_dict.values())

        def show_Information_per_room(self, nights:int) -> list[dict]:
            query = """
                SELECT 
                    Room.room_id,
                    Room_Type.description,
                    Room_Type.max_guests,
                    GROUP_CONCAT(Facilities.facility_name, ', ') AS ausstattung,
                    Room.price_per_night
                FROM Room
                JOIN Room_Type ON Room.type_id = Room_Type.type_id
                LEFT JOIN Room_Facilities ON Room.room_id = Room_Facilities.room_id
                LEFT JOIN Facilities ON Room_Facilities.facility_id = Facilities.facility_id
                GROUP BY Room.room_id, Room_Type.description, Room_Type.max_guests, Room.price_per_night
                ORDER BY Room.room_id;
            """
            results = self.fetchall(query)
            zimmer_liste = []

            for row in results:
                room_id, zimmertyp, max_guests, ausstattung, preis_pro_nacht = row
                ausstattung = ausstattung or "Keine"
                gesamtpreis = preis_pro_nacht * nights
                zimmer_liste.append({
                    "Zimmer-ID": room_id,
                    "Zimmertyp": zimmertyp,
                    "Max. Gäste": max_guests,
                    "Ausstattung": ausstattung,
                    "Preis pro Nacht (CHF)": preis_pro_nacht,
                    f"Gesamtpreis für {nights} Nächte (CHF)": gesamtpreis
                })

            return zimmer_liste


        def zeige_verfuegbare_zimmer(self, check_in_date: str, check_out_date: str) -> list[dict]:
            query = """
                SELECT 
                    Room.room_id,
                    Room_Type.description,
                    Room_Type.max_guests,
                    GROUP_CONCAT(Facilities.facility_name) AS ausstattung,
                    Room.price_per_night
                FROM Room
                JOIN Room_Type ON Room.type_id = Room_Type.type_id
                LEFT JOIN Room_Facilities ON Room.room_id = Room_Facilities.room_id
                LEFT JOIN Facilities ON Room_Facilities.facility_id = Facilities.facility_id
                WHERE Room.room_id NOT IN (
                    SELECT room_id
                    FROM Booking
                    WHERE is_cancelled = 0
                    AND check_in_date < ?
                    AND check_out_date > ?
                )
                GROUP BY Room.room_id, Room_Type.description, Room_Type.max_guests, Room.price_per_night
                ORDER BY Room.room_id;
            """
            results = self.fetchall(query, (check_out_date, check_in_date))
            zimmer_liste = []

            for row in results:
                room_id, zimmertyp, max_guests, ausstattung, preis_pro_nacht = row
                ausstattung = (ausstattung or "Keine").replace(",", ", ")
                zimmer_liste.append({
                    "Zimmer-ID": room_id,
                    "Zimmertyp": zimmertyp,
                    "Max. Gäste": max_guests,
                    "Ausstattung": ausstattung,
                    "Preis pro Nacht (CHF)": preis_pro_nacht,
                })

            return zimmer_liste

        def read_hotels_by_city(self, city):
            sql = """
            SELECT hotel_id, name, stars, Address.address_id, street, city, zip_code FROM Hotel
            JOIN Address ON Address.address_id = Hotel.address_id
            WHERE UPPER(Address.city) = ?
            """
            params = (city,)
            results = self.fetchall(sql, params)
            hotels = []
            for row in results:
                hotel_id, name, stars, address_id, street, city_name, zip_code = row
                address = Address(address_id, street, city_name, zip_code)
                hotel = Hotel(hotel_id, name, stars, address)
                hotels.append(hotel)
            return hotels

        def update_hotel(self, hotel_id: int, name: str, stars: int, address_id: int) -> bool:
            if not hotel_id:
                raise ValueError("Hotel-ID ist erforderlich")
            if not name:
                raise ValueError("Hotelname darf nicht leer sein")
            if stars < 1 or stars > 5:
                raise ValueError("Sterne müssen zwischen 1 und 5 liegen")
            if not address_id:
                raise ValueError("Address-ID ist erforderlich")

            sql = """
                UPDATE Hotel
                SET name = ?, stars = ?, address_id = ?
                WHERE hotel_id = ?;
                """
            params = (name, stars, address_id, hotel_id)
            _, row_count = self.execute(sql, params)

            return row_count > 0




        def delete_hotel(self, hotel_id) -> bool:
            if not hotel_id:
                raise ValueError("Hotel ID is required")

            sql = """
            DELETE FROM Hotel
            WHERE hotel_id = ?;
            """
            params = (hotel_id, )
            _, row_count = self.execute(sql, params)
            return row_count > 0


        def read_hotel_by_id(self, hotel_id):
            pass

        def create_new_hotel(self, name: str, stars:int, address: model.Address) -> list[model.Hotel]:
            if name is None:
                raise ValueError("Hotel name is required")
            if stars is None:
                raise ValueError("Hotel stars is required")
            if address is None:
                raise ValueError("Hotel address is required")

            sql = """
            INSERT INTO Hotel (name, stars, address_id)
            VALUES (?, ?, ?)
            """
            address_id = address.address_id
            params = (name, stars, address.address_id)
            last_row_id, row_count = self.execute(sql, params)
            return model.Hotel (
                hotel_id=last_row_id,
                name =name,
                stars = stars,
                address = address)

        def get_dynamic_room_prices(self, check_in_date: date, check_out_date: date) -> list[dict]:

            query = """
                SELECT
                    r.room_id,
                    r.room_number,
                    rt.description,
                    rt.max_guests,
                    r.price_per_night,
                    CASE
                        WHEN DATE(?) BETWEEN DATE('2025-07-01') AND DATE('2025-08-31') THEN ROUND(r.price_per_night * 1.2, 2)
                        WHEN DATE(?) BETWEEN DATE('2025-12-20') AND DATE('2026-01-05') THEN ROUND(r.price_per_night * 1.3, 2)
                        ELSE r.price_per_night
                    END AS dynamic_price,
                    h.name AS hotel_name,
                    a.city,
                    a.street,
                    a.zip_code
                FROM Room r
                JOIN Room_Type rt ON r.type_id = rt.type_id
                JOIN Hotel h ON r.hotel_id = h.hotel_id
                JOIN Address a ON h.address_id = a.address_id
                ORDER BY dynamic_price ASC
            """

            results = self.fetchall(query, (check_in_date, check_out_date))
            zimmerliste = []

            for row in results:
                (
                    room_id, room_number, room_type, max_guests, base_price,
                    dynamic_price, hotel_name, city, street, zip_code
                ) = row

                zimmerliste.append({
                    "Hotel": hotel_name,
                    "Zimmernummer": room_number,
                    "Zimmertyp": room_type,
                    "Max. Gäste": max_guests,
                    "Basispreis (CHF)": base_price,
                    "Dynamischer Preis (CHF)": dynamic_price,
                    "Stadt": city,
                    "Adresse": f"{street}, {zip_code}",
                    "Check-in": check_in_date
                })

            return zimmerliste

        def get_room_type_popularity(self) -> pd.DataFrame:
            query = """
                SELECT rt.description AS room_type, COUNT(*) AS total_bookings
                FROM Booking b
                JOIN Room r ON b.room_id = r.room_id
                JOIN Room_Type rt ON r.type_id = rt.type_id
                WHERE b.is_cancelled = 0
                GROUP BY rt.description
            """
            rows = self.fetchall(query)


            df = pd.DataFrame(rows, columns=["room_type", "total_bookings"])
            return df


