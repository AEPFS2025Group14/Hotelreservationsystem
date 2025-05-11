class Facility:
    def __init__(self, facility_id: int, facility_name: str):
        if not facility_id:
            raise ValueError("Facility ID is required")
        if not isinstance(facility_id, int):
            raise ValueError("Facility ID must be an integer")
        if not facility_name:
            raise ValueError("Facility name is required")
        if not isinstance(facility_name, str):
            raise TypeError("Facility name must be an string")


        self.facility_id : int = facility_id
        self.facility_name : str = facility_name

    def __repr__(self):
        return (f"Facility(id={self.facility_id}, name='{self.facility_name})")

    @property
    def facility_id(self) -> int:
        return self.__facility_id
    @property
    def facility_name(self) -> str:
        return self.__facility_name
    @facility_name.setter
    def facility_name(self, facility_name: str) -> None:
        if not facility_name:
            raise ValueError("Facility name is required")
        if not isinstance(facility_name, str):
            raise ValueError("Facility name must be an string")
        self.__facility_name = facility_name
