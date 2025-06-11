import model
import data_access


class RoomManager:
    def __init__(self):
        self.__room_da = data_access.RoomDataAccess()

    def create_room(self,
                    room_number: str,
                    hotel: model.Hotel,
                    room_type: model.RoomType,
                    price_per_night: float
                    ) -> model.Room:
        return self.__room_da.create_new_room(
            room_number=room_number,
            hotel=hotel,
            room_type=room_type,
            price_per_night=price_per_night
        )

    def get_room_by_id(self, room_id: int) -> [model.Room]:
        return self.__room_da.get_room_by_id(room_id)

    def read_rooms_by_hotel(self, hotel: model.Hotel) -> list[model.Room]:
        return self.__room_da.read_rooms_by_hotel(hotel)

    def get_rooms_with_facilities(self) -> list[dict]:
        return self.__room_da.get_rooms_with_facilities()

    def update_price(self, room_id: int, new_price: float) -> bool:
        return self.__room_da.update_price(room_id=room_id, new_price=new_price)