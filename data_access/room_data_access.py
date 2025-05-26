import model
from data_access.base_data_access import BaseDataAccess
from data_access.room_type_data_access import RoomTypeDataAccess


class RoomDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)
        self.__room_type_da = RoomTypeDataAccess()

    def create_new_room(self,
                        room_number: str,
                        hotel: model.Hotel,
                        room_type: model.RoomType,
                        price_per_night: float) -> model.Room:
        if not all([room_number, hotel, room_type, price_per_night is not None]):
            raise ValueError("All room fields are required")

        sql = """
        INSERT INTO Room (room_number, hotel_id, type_id, price_per_night)
        VALUES (?, ?, ?, ?)
        """
        params = (room_number, hotel.hotel_id, room_type.type_id, price_per_night)
        last_row_id, _ = self.execute(sql, params)

        return model.Room(room_id=last_row_id,
                          room_number=room_number,
                          hotel=hotel,
                          room_type=room_type,
                          price_per_night=price_per_night)

    def read_room_by_id(self, room_id: int) -> model.Room | None:
        sql = """
        SELECT room_id, room_number, hotel_id, type_id, price_per_night
        FROM Room WHERE room_id = ?
        """
        result = self.fetchone(sql, (room_id,))
        if result:
            room_id, room_number, hotel_id, type_id, price_per_night = result
            return model.Room(room_id, room_number, hotel_id, type_id, price_per_night)
        return None

    def read_rooms_by_hotel(self, hotel: model.Hotel) -> list[model.Room]:
        sql = """
        SELECT room_id, room_number, type_id, price_per_night
        FROM Room WHERE hotel_id = ?
        """
        rows = self.fetchall(sql, (hotel.hotel_id,))
        rooms = []
        for row in rows:
            room_id, room_number, type_id, price_per_night = row
            print(type(room_id))
            room_type = self.__room_type_da.read_room_type_by(type_id)
            room = model.Room(room_id, room_number, room_type)
            rooms.append(room)
        return rooms