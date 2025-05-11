import model
import data_access


class RoomTypeManager:
    def __init__(self):
        self.__room_type_da = data_access.RoomTypeDataAccess()

    def read_room_type_by_name(self, type_name: str) -> model.RoomType | None:
        return self.__room_type_da.read_room_type_by_name(type_name)

    def read_all_room_types(self) -> list[model.RoomType]:
        return self.__room_type_da.read_all_room_types()
