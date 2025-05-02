class RoomFacility:
    def __init__(self, room_id: int, facility_id: int):
        self.__room_id = room_id
        self.__facility_id = facility_id

    @property
    def room_id(self):
        return self.__room_id

    @property
    def facility_id(self):
        return self.__facility_id
