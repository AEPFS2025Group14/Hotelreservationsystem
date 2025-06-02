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

    def read_room(self, room_id: int) -> model.Room:
        return self.__room_da.read_room_by_id(room_id)

    def read_rooms_by_hotel(self, hotel: model.Hotel) -> list[model.Room]:
        return self.__room_da.read_rooms_by_hotel(hotel)


