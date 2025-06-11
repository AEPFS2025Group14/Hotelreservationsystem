from datetime import datetime, date
import model
from model import Hotel
from model.room_type import RoomType
from model.address import Address
import data_access
from business_logic.room_type_manager import RoomTypeManager
from model.hotel import Hotel
from business_logic.validation_functions import Validation_functions

from business_logic.booking_manager import BookingManager


class HotelManager:
    def __init__(self) -> None:
        self.__hotel_da = data_access.HotelDataAccess()
        self.__room_type_manager = RoomTypeManager()

    def create_new_hotel(self, name: str, stars: int, address: Address = None) -> list[Hotel]:
        Validation_functions.validate_name(name)
        Validation_functions.validate_stars(stars)
        return self.__hotel_da.create_new_hotel(name=name, stars=stars, address=address)


    def search_hotels_by_city(self, city: str) -> list[model.Hotel]:
        Validation_functions.validate_city(city)
        city = Validation_functions.normalize_city(city)
        return self.__hotel_da.search_hotels_by_city(city)

    def search_hotels_by_city_and_stars(self, city: str, stars: int) -> list[model.Hotel]:
        Validation_functions.validate_city(city)
        Validation_functions.validate_stars(stars)
        city = Validation_functions.normalize_city(city)
        return self.__hotel_da.search_hotels_by_city_and_stars(city, stars)

    def update_hotel(self, hotel_id: int, name: str, stars: int, address_id: int) -> bool:
        Validation_functions.validate_name(name)
        Validation_functions.validate_stars(stars)

        return self.__hotel_da.update_hotel(hotel_id, name=name, stars=stars, address_id=address_id)

    def delete_hotel(self, hotel_id) -> bool:
        return self.__hotel_da.delete_hotel(hotel_id)

    def search_hotels_for_guests(self, city: str, stars: int, max_guests: int, room_typ_id=None,
                                  description=None) -> list[model.Hotel]:
        Validation_functions.validate_city(city)
        Validation_functions.validate_stars(stars)
        Validation_functions.validate_max_guests(max_guests)
        city = Validation_functions.normalize_city(city)
        return self.__hotel_da.search_hotels_for_guests(city, stars, max_guests, room_typ_id, description)

    def search_hotel_Aufenthalt(self, city: str, check_in: date, check_out: date) -> list[model.Hotel]:
        Validation_functions.validate_city(city)
        Validation_functions.validate_booking_dates(check_in, check_out)
        city = Validation_functions.normalize_city(city)
        return self.__hotel_da.search_hotel_Aufenthalt(city, check_in.isoformat(), check_out.isoformat())

    def search_hotel_combinated(self, city: str, check_in_date: str, check_out_date: str,
                                 min_stars: int = 0, max_guests: int = None) -> list[model.Hotel]:

        check_in, check_out = Validation_functions.parse_and_validate_dates(check_in_date, check_out_date)
        Validation_functions.validate_city(city)
        Validation_functions.validate_stars(min_stars)
        Validation_functions.validate_max_guests(max_guests)
        city = Validation_functions.normalize_city(city)
        return self.__hotel_da.search_hotel_combinated(city, check_in_date, check_out_date, min_stars, max_guests)

    def zeige_Information_pro_Hotel(self) -> list[model.Hotel]:
        return self.__hotel_da.zeige_Information_pro_Hotel()


    def search_hotel_print_rooms(self, city: str, check_in_date: str = None, check_out_date: str = None,
                                 description=None, max_guests=None, room_type_id=None,
                                 address_id=None, zip_code=None, street=None, room_number=None) -> list[model.Hotel]:

        Validation_functions.validate_city(city)
        city = Validation_functions.normalize_city(city)


        check_in = check_out = None
        if check_in_date and check_out_date:
            check_in, check_out = Validation_functions.parse_and_validate_dates(check_in_date, check_out_date)


        if max_guests is not None:
            Validation_functions.validate_max_guests(max_guests)


        return self.__hotel_da.search_hotel_print_rooms(city=city,check_in_date=check_in, check_out_date=check_out,
            description=description, max_guests=max_guests, room_type_id=room_type_id,
            address_id=address_id, zip_code=zip_code, street=street, room_number=room_number
        )

    def show_Information_per_room(self, nights: int) -> list[dict]:
        return self.__hotel_da.show_Information_per_room(nights)

    def zeige_verfuegbare_zimmer(self, check_in_date: str, check_out_date: str) -> list[dict]:
        check_in, check_out = Validation_functions.parse_and_validate_dates(check_in_date, check_out_date)
        return self.__hotel_da.zeige_verfuegbare_zimmer(check_in_date, check_out_date)

    def get_dynamic_room_prices(self, check_in_date: str = None, check_out_date: str = None) -> list[dict]:
        check_in = check_out = None
        if check_in_date and check_out_date:
            check_in, check_out = Validation_functions.parse_and_validate_dates(check_in_date, check_out_date)

        return self.__hotel_da.get_dynamic_room_prices(
            check_in_date=check_in.isoformat(),
            check_out_date=check_out.isoformat()
        )
