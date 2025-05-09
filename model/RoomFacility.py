class RoomFacility:
    def __init__(self, room_id: int, facility_id: int):
        if not room_id:
            raise ValueError("Room ID is required")
        if not isinstance(room_id, int):
            raise ValueError("Room ID must be an integer")
        if not facility_id:
            raise ValueError("Facility ID is required")
        if not isinstance(facility_id, int):
            raise ValueError("Facility ID must be an integer")


        self.__room_id : int  = room_id
        self.__facility_id : int = facility_id

    def __repr__(self):
        return (f"RoomFacility(room_id={self.__room_id}, facility_id={self.facility_id})")
