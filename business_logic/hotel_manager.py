import os
import pandas as pd

import model
import data_access
from business_logic.room_type_manager import RoomTypeManager
from model.hotel import Hotel


class HotelManager:
    def __init__(self) -> None:
        self.__hotel_da = data_access.HotelDataAccess()
        self.__room_type_manager = RoomTypeManager()


    def create_hotel(self, name: str, stars: int) -> model.Hotel:
        pass
        #return self.__hotel_da.create_new_hotel(name, stars)

    def read_hotel(self, hotel_id: int) -> model.Hotel:
        return self.__hotel_da.read_hotel_by_id(hotel_id)

    def read_hotels_by_city(self, city: str) -> list[model.Hotel]:
        return self.__hotel_da.read_hotels_by_city(city)

    def search_hotels_by_city_and_stars(self, city: str, stars: int) -> list[model.hotel]:
        return self.__hotel_da.search_hotels_by_city_and_stars(city, stars)

    def search_hotels_by_city(self, city: str) -> list[model.hotel]:
        return self.__hotel_da.search_hotels_by_city(city)

    def update_hotel(self, hotel: model.hotel) -> None:
        self.__hotel_da.update_hotel(hotel)

    def delete_hotel(self, hotel : model.hotel) -> None:
        self.__hotel_da.delete_hotel(hotel)

    def search_hotels_for_guests(self, city: str, stars: int, max_guests :int ) -> list[model.Hotel]:
        return self.__hotel_da.search_hotels_for_guests(city, stars, max_guests)

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

