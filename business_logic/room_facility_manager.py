import model
import data_access


class RoomFacilityManager:
    def __init__(self):
        self.__room_facility_da = data_access.RoomFacilityDataAccess()

    def add_facility_to_room(self, room: model.Room, facility: model.Facility) -> None:
        self.__room_facility_da.add_facility_to_room(room, facility)

    def read_facilities_by_room(self, room: model.Room) -> list[model.Facility]:
        return self.__room_facility_da.read_facilities_by_room(room)

    def remove_facility_from_room(self, room: model.Room, facility: model.Facility) -> None:
        self.__room_facility_da.remove_facility_from_room(room, facility)

    def update_facility(self, facility_id: int, facility_name: str) -> bool:
        if not facility_name or facility_id < 0:
            raise ValueError("Name is required")
        return self.__room_facility_da.update_facility(facility_id, facility_name)
