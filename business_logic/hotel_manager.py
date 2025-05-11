import os

import model
import data_access


class HotelManager:
    def __init__(self) -> None:
        self.__hotel_da = data_access.HotelDataAccess()

    def create_hotel(self, name: str, stars: int, address: model.Address) -> model.Hotel:
        return self.__hotel_da.create_new_hotel(name, stars, address)

    def read_hotel(self, hotel_id: int) -> model.Hotel:
        return self.__hotel_da.read_hotel_by_id(hotel_id)

    def read_hotels_by_city(self, city: str) -> list[model.Hotel]:
        return self.__hotel_da.read_hotels_by_city(city)

    def update_hotel(self, hotel: model.Hotel) -> None:
        self.__hotel_da.update_hotel(hotel)

    def delete_hotel(self, hotel_id: int) -> None:
        self.__hotel_da.delete_hotel(hotel_id)
