class Facility:
    def __init__(self, facility_id: int, facility_name: str):
        self.__facility_id = facility_id
        self.__facility_name = facility_name

    @property
    def facility_id(self):
        return self.__facility_id

    @property
    def facility_name(self):
        return self.__facility_name

    @facility_name.setter
    def facility_name(self, facility_name):
        self.__facility_name = facility_name
