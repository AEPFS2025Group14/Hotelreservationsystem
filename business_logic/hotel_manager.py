import os
import pandas as pd

import model
from model.room_type import RoomType
from model.address import Address
import data_access
from business_logic.room_type_manager import RoomTypeManager
from model.hotel import Hotel


class HotelManager:
    def __init__(self) -> None:
        self.__hotel_da = data_access.HotelDataAccess()
        self.__room_type_manager = RoomTypeManager()

    def create_new_hotel(self, name:str, stars:int, address:Address =None) -> model.Hotel:
        return self.__hotel_da.create_new_hotel(name= name, stars = stars, address = address)

    def read_hotel(self, hotel_id: int) -> model.Hotel:
        return self.__hotel_da.read_hotel_by_id(hotel_id)

    def read_hotels_by_city(self, city: str) -> list[model.Hotel]:
        return self.__hotel_da.read_hotels_by_city(city)

    def search_hotels_by_city_and_stars(self, city: str, stars: int) -> list[model.Hotel]:
        return self.__hotel_da.search_hotels_by_city_and_stars(city, stars)

    def search_hotels_by_city(self, city: str) -> list[model.Hotel]:
        return self.__hotel_da.search_hotels_by_city(city)

    def update_hotel(self, hotel_id: int, name: str, stars: int, address_id : int) -> bool:
        return self.__hotel_da.update_hotel(hotel_id, name = name, stars = stars, address_id = address_id)

    def delete_hotel(self, hotel_id) -> bool:
        return self.__hotel_da.delete_hotel(hotel_id)

    def search_hotels_for_guests(self, city: str, stars: int, max_guests: int, room_typ_id=None,
                                     description=None) -> list[model.Hotel]:
        return self.__hotel_da.search_hotels_for_guests(city, stars, max_guests, room_typ_id, description)

    def search_hotel_Aufenthalt(self, city: str, check_in_date: str, check_out_date: str) -> list[model.Hotel]:
        return self.__hotel_da.search_hotel_Aufenthalt(city, check_in_date, check_out_date)

    def search_hotel_combinated(self, city: str, check_in_date: str, check_out_date: str,
                                min_stars: int = 0, max_guests: int = None) -> list[model.Hotel]:
        return self.__hotel_da.search_hotel_combinated(city, check_in_date, check_out_date, min_stars, max_guests)

    def zeige_Information_pro_Hotel(self) -> list[model.Hotel]:
        return self.__hotel_da.zeige_Information_pro_Hotel()

    def search_hotel_print_rooms(self, city: str, description=None, max_guests=None, room_typ_id=None,
                                 address_id=None, zip_code=None, street=None) -> list[model.Hotel]:
        return self.search_hotel_print_rooms(city, description, max_guests, room_typ_id)

    def show_Information_per_room(self, nights: int) -> list[dict]:
        return self.__hotel_da.show_Information_per_room(nights)

    def zeige_verfuegbare_zimmer(self, check_in_date: str, check_out_date: str) -> list[dict]:
        return self.__hotel_da.zeige_verfuegbare_zimmer(check_in_date, check_out_date)

    def all_room_types(self, hotel: Hotel) -> list[model.RoomType]:
        room_type_ids_of_hotel: list[int] = []
        for room in hotel.rooms:
            if room.room_type.room_type_id not in room_type_ids_of_hotel:
                room_type_ids_of_hotel.append(room.room_type.room_type_id)

        room_types = []
        for room_type_id in room_type_ids_of_hotel:
            room_type = self.__room_type_manager.read_room_type_by_id(room_type_id)
            room_types.append(room_type)
        return room_types

