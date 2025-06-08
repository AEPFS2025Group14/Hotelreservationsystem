import model
from data_access.base_data_access import BaseDataAccess


class RoomFacilityDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def add_facility_to_room(self, room: model.Room, facility: model.Facility) -> None:
        if not room or not facility:
            raise ValueError("Room and Facility are required")

        sql = """
        INSERT INTO Room_Facilities (room_id, facility_id)
        VALUES (?, ?)
        """
        self.execute(sql, (room.room_id, facility.facility_id))

    def read_facilities_by_room(self, room: model.Room) -> list[model.Facility]:
        sql = """
        SELECT f.facility_id, f.facility_name
        FROM Facilities f
        JOIN Room_Facilities rf ON f.facility_id = rf.facility_id
        WHERE rf.room_id = ?
        """
        rows = self.fetchall(sql, (room.room_id,))
        return [model.Facility(facility_id, name) for facility_id, name in rows]

    def remove_facility_from_room(self, room: model.Room, facility: model.Facility) -> None:
        sql = """
        DELETE FROM Room_Facilities WHERE room_id = ? AND facility_id = ?
        """
        self.execute(sql, (room.room_id, facility.facility_id))

    def update_facility(self, facility_id: int, facility_name: str) -> bool:
        sql = """
        UPDATE Facilities 
        SET facility_name = ?
        WHERE facility_id = ?
        """
        params = (facility_name, facility_id)
        _, row_count = self.execute(sql, params)
        return row_count >0