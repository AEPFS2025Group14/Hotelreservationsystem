import model
from data_access.base_data_access import BaseDataAccess


class FacilitiesDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def read_facility_by_name(self, name: str) -> model.Facility | None:
        sql = "SELECT facility_id, facility_name FROM Facilities WHERE facility_name = ?"
        result = self.fetchone(sql, (name,))
        if result:
            return model.Facility(*result)
        return None

    def read_all_facilities(self) -> list[model.Facility]:
        sql = "SELECT facility_id, facility_name FROM Facilities ORDER BY facility_id"
        facilities = self.fetchall(sql)
        return [model.Facility(facility_id, name) for facility_id, name in facilities]
