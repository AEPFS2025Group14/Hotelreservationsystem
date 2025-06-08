import model
import data_access


class RoomTypeManager:
    def __init__(self):
        self.__room_type_da = data_access.RoomTypeDataAccess()

    def read_room_type_by_id(self, type_id: int) -> model.RoomType:
        return self.__room_type_da.read_room_type_by(type_id)

    def search_room_by_type(self, description: str) -> model.Room:
        return self.__room_type_da.search_room_by_type(description)

    def update_room_type(self, type_id: int, description: str, max_guests: int) -> bool:
        if not description or max_guests <= 0:
            raise ValueError("Ungültige Eingabewerte für den Zimmertyp")
        return self.__room_type_da.update_room_type(type_id, description, max_guests)