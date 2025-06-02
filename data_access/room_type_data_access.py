import model
from data_access.base_data_access import BaseDataAccess


class RoomTypeDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def read_room_type_by(self, room_type_id: int) -> model.RoomType:
        sql = """
        SELECT type_id, description, max_guests FROM Room_Type
        WHERE type_id = ?
        """
        params = tuple([room_type_id])
        result = self.fetchone(sql, params)
        type_id, description, max_guests = result
        return model.RoomType(type_id, description, max_guests)

