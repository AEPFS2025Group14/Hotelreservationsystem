import model
from data_access.base_data_access import BaseDataAccess
from data_access.room_type_data_access import RoomTypeDataAccess
from model import RoomType


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

    def get_room_by_id(self, room_id: int) -> [model.Room]:
        sql = """
        SELECT r.room_id, r.room_number, r.price_per_night,
               rt.type_id, rt.description, rt.max_guests
        FROM Room r
        JOIN Room_Type rt ON r.type_id = rt.type_id
        WHERE r.room_id = ?
        """
        params = (room_id,)
        result = self.fetchone(sql, params)

        if result:
            room_id, room_number, price_per_night, type_id, description, max_guests = result
            room_type = model.RoomType(type_id, description, max_guests)
            return model.Room(room_id, room_number, room_type, price_per_night)
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
            room = model.Room(room_id, room_number, room_type, price_per_night=price_per_night)
            rooms.append(room)
        return rooms

    def get_rooms_with_facilities(self) -> list[dict]:
        sql = """ 
        SELECT r.room_id, r.room_number, h.name AS hotel_name,
        GROUP_CONCAT(f.facility_name) AS facility_name
        FROM room r 
        JOIN Hotel h ON r.hotel_id = h.hotel_id
        LEFT JOIN Room_Facilities rf ON r.room_id = rf.room_id
        LEFT JOIN Facilities f ON rf.facility_id = f.facility_id
        GROUP BY r.room_id, r.room_number, h.name 
        ORDER BY r.room_id
        """

        result = self.fetchall(sql)
        zimmerliste = []
        for row in result:
            room_id, room_number, hotel_name, ausstattung = row
            zimmerliste.append({
                "Zimmer-ID" : room_id,
                "Zimmernummer" : room_number,
                "Hotel" : hotel_name,
                "Ausstattung" : ausstattung or "Keine"
            })

        return zimmerliste

    def update_price(self, room_id: int, new_price: float) -> bool:
        sql = """
        UPDATE Room 
        SET price_per_night = ?
        WHERE room_id = ?
        """
        params = (new_price, room_id)
        _, row_count = self.execute(sql, params)
        return row_count > 0





