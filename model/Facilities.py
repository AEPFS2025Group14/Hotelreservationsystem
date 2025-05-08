class Facility:
    def __init__(self, facility_id: int, facility_name: str):
        self.facility_id = facility_id
        self.facility_name = facility_name

    def __str__(self):
        return f"Facility(id={self.facility_id}, name='{self.facility_name}')"
