from model import Room


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
        if Room is not None:
            Room.add_facility(self)

    def __repr__(self):
        return (f"RoomFacility(room_id={self.__room_id}, facility_id={self.facility_id})")


    @property
    def Room(self) -> Room:
        return self.__room_id

    @Room.setter
    def Room(self, rooom : Room) -> None:
        if self.__room is not Room:
            if self.__room is not None:
                self.__room.remove_RoomFacility(self)
            self.__room = Room

            if Room is not None and self not in Room.RoomFacility:
                Room.add_facility(self)




    raise ValueError("Room must be an instance of Room")
