import model
import data_access


class FacilitiesManager:
    def __init__(self):
        self.__facilities_da = data_access.FacilitiesDataAccess()


    def read_all_facilities(self) -> list[model.Facility]:
        return self.__facilities_da.read_all_facilities()
