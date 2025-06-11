import model
import data_access
from business_logic.validation_functions import Validation_functions


class AddressManager:
    def __init__(self) -> None:
        self.__address_da = data_access.AddressDataAccess()

    def create_new_address(self, street: str, city: str, zip_code: str) -> model.Address:
        Validation_functions.validate_street(street)
        Validation_functions.validate_city(city)
        Validation_functions.validate_zip_code(zip_code)
        return self.__address_da.create_new_address(street=street, city=city, zip_code=zip_code)

    def read_address_by_id(self, address_id: int) -> model.Address | None:
        result = self.__address_da.read_address_by_id(address_id)
        if result:
            return model.Address(*result)
        return None