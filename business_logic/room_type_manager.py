import model
import data_access


class RoomTypeManager:
    def __init__(self):
        self.__room_type_da = data_access.RoomTypeDataAccess()

    def read_room_type_by_id(self, type_id: int) -> model.RoomType:
        return self.__room_type_da.read_room_type_by(type_id)

    def search_room_by_type(self, description: str) -> model.Room:
        return self.__room_type_da.search_room_by_type(description)
