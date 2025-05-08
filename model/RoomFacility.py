class RoomFacility:
    def __init__(self, room_id: int, facility_id: int):
        self.room_id = room_id
        self.facility_id = facility_id

    def __str__(self):
        return f"RoomFacility(room_id={self.room_id}, facility_id={self.facility_id})"
