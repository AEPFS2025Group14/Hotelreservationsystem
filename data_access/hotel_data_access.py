import model
from model import RoomType, Room, address
from .base_data_access import BaseDataAccess
from .room_data_access import RoomDataAccess
from model.hotel import Hotel
from model.address import Address


class HotelDataAccess(BaseDataAccess):
        def __init__(self, db_path: str = None):
            super().__init__(db_path)
            self.__room_da = RoomDataAccess()

        def search_hotels_by_city(self, city: str) -> list[model.hotel]:

            query = """
                    SELECT h.hotel_id, h.name, h.stars, a.address_id, a.city, a.street, a.zip_code
                    FROM Hotel h
                    JOIN Address a ON h.address_id = a.address_id
                    WHERE a.city = ?
                """
            results = self.fetchall(query, (city,))
            hotels = []
            for row in results:
                hotel_id, name, stars, address_id, city, street, zip_code = row
                address = Address(address_id, street, city, zip_code)
                hotel = Hotel(hotel_id, name, stars, address)
                hotels.append(hotel)
            return hotels

        def search_hotels_by_city_and_stars(self, city: str, stars: int) -> list[model.hotel]:

                query = """ 
                    SELECT h.hotel_id, h.name, h.stars, a.address_id, a.city, a.street, a.zip_code
                    FROM Hotel h
                    JOIN Address a ON h.address_id = a.address_id
                    WHERE a.city = ? AND h.stars = ?;
                    """

                results = self.fetchall(query, (city, stars))
                hotels = []
                for row in results:
                    hotel_id, name, stars, address_id, city, street, zip_code = row
                    address = Address(address_id, street, city, zip_code)
                    hotel = Hotel(hotel_id, name, stars, address)
                    hotels.append(hotel)
                return hotels

        def search_hotels_for_guests(self, city: str, stars: int, max_guests: int, room_typ_id=None, description = None) -> list[model.hotel]:

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
                        a.city = ? AND h.stars = ? AND rt.max_guests >= ?;
                """
                results = self.fetchall(query, (city, stars, max_guests))
                hotels = []

                for row in results:
                    description, max_guests, room_type_id, name, stars, hotel_id, address_id, city, street, zip_code = row

                    room_type = RoomType(room_type_id, description, max_guests)
                    address = Address(address_id, street, city, zip_code)
                    hotel = Hotel(hotel_id, name, stars, address)
                    hotel.room_type = room_type
                    hotels.append(hotel)
                return hotels

        def search_hotel_Aufenthalt(self, city: str, check_in_date: str, check_out_date :str) -> list[model.hotel]:
                sql = """
                    SELECT Room.room_id, Room.room_number, Room_Type.description, Room_Type.max_guests, Room_Type.type_id,
                           Hotel.name, Hotel.stars, Room.price_per_night, Hotel.hotel_id,
                           Address.address_id, Address.street, Address.city, Address.zip_code 
                    FROM Hotel 
                    JOIN Room ON Hotel.hotel_id = Room.hotel_id
                    JOIN Room_Type ON Room.type_id = Room_Type.type_id
                    JOIN Address ON Hotel.address_id = Address.address_id
                    WHERE Address.city = ?
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
                                  min_stars: int = 0, max_guests: int = None) -> list[model.hotel]:
                sql = """
                    SELECT Room.room_id, Room.room_number, Room_Type.description, Room_Type.max_guests, Room_Type.type_id,
                           Hotel.name, Hotel.stars, Room.price_per_night, Hotel.hotel_id,
                           Address.address_id, Address.street, Address.city, Address.zip_code 
                    FROM Hotel 
                    JOIN Room ON Hotel.hotel_id = Room.hotel_id
                    JOIN Room_Type ON Room.type_id = Room_Type.type_id
                    JOIN Address ON Hotel.address_id = Address.address_id
                    WHERE Address.city = ?
                      AND Hotel.stars >= ?
                      AND Room.room_id NOT IN (
                          SELECT room_id
                          FROM Booking
                          WHERE is_cancelled = 0
                            AND NOT (? <= check_in_date OR ? >= check_out_date)
                      )
                """

                params = [city, min_stars, check_out_date, check_in_date]

                if max_guests is not None:
                    sql += " AND Room_Type.max_guests >= ?"
                    params.append(max_guests)

                results = self.fetchall(sql, params)
                hotel_map = {}

                for row in results:
                    for row in results:
                        (
                            room_id, room_number, description, max_guests_row, room_type_id,
                            name, stars, price_per_night, hotel_id,
                            address_id, street, city_name, zip_code
                        ) = row

                        if max_guests_row < max_guests:
                            continue  # Zimmer bietet nicht genug Platz

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
                                existing_hotel.rooms = [room]  # Günstigeres Zimmer ersetzen

                    return list(hotel_map.values())

        def zeige_Information_pro_Hotel(self) -> list[model.hotel]:

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


        def search_hotel_print_rooms(self, city: str, description=None, max_guests=None, room_type_id=None,
                                     address_id=None, zip_code=None, street=None, room_number=None) -> list[model.hotel]:
                query = """
                    SELECT Room.room_id, Room.room_number, Room_Type.description, Room_Type.max_guests, Room_Type.type_id,
                            Hotel.name, Hotel.stars, Room.price_per_night, Hotel.hotel_id, Address.address_id, Address.street, Address.city, Address.zip_code 
                    FROM Hotel 
                    JOIN ROOM ON Hotel.hotel_id = Room.hotel_id
                    JOIN Room_Type Room_Type ON Room.type_id = Room_Type.type_id
                    JOIN Address ON Hotel.address_id = Address.address_id
                    WHERE Address.city = ?    
                """
                results = self.fetchall(query, (city,))
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
            WHERE Address.city = ?
            """
            params = tuple([city])
            results = self.fetchall(sql, params)
            hotels = []
            for row in results:
                room_id, room_number, description, max_guests, room_type_id, name, stars, price_per_night, hotel_id = row

                room_type = RoomType(room_type_id, description, max_guests)
                room = Room(room_id, room_number, room_type, price_per_night)

                address = None  # wenn nicht im SELECT enthalten
                hotel = Hotel(hotel_id, name, stars, address)
                hotel.rooms = [room]

                hotels.append(hotel)
            return hotels

        def update_hotel(self, hotel):
            pass

        def delete_hotel(self, hotel):
            pass

        def read_hotel_by_id(self, hotel_id):
            pass

        def create_new_hotel(self, name, stars, address):
            pass




