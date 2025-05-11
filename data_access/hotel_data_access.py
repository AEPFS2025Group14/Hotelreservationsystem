from .base_data_access import BaseDataAccess
from model.hotel import Hotel
from model.address import Address


class HotelDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def search_hotels_by_city(self, city: str) -> list[Hotel]:
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
