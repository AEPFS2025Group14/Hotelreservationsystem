import model
from .base_data_access import BaseDataAccess
from model.hotel import Hotel
from model.address import Address


class HotelDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)


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

    def search_hotels_for_guests(self, city: str, stars: int, max_guests: int) -> list[model.hotel]:
            query = """
                SELECT
                    h.hotel_id, h.name, h.stars, a.address_id, a.city, a.street, a.zip_code, rt.max_guests
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
                hotel_id, name, stars, address_id, city, street, zip_code, max_guests = row
                address = Address(address_id, street, city, zip_code)
                hotel = Hotel(hotel_id, name, stars, address)
                hotels.append(hotel)
            return hotels


    def read_hotels_by_city(self, city):
        pass

    def update_hotel(self, hotel):
        pass

    def delete_hotel(self, hotel):
        pass

    def read_hotel_by_id(self, hotel_id):
        pass

    def create_new_hotel(self, name, stars, address):
        pass
    