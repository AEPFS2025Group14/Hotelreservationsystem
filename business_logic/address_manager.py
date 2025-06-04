import model
import data_access


class AddressManager:
    def __init__(self) -> None:
        self.__address_da = data_access.AddressDataAccess()

    def create_new_address(self,  street:str, city:str, zip_code:str) -> model.Address:
        return self.__address_da.create_new_address(street=street, city=city, zip_code=zip_code)

    def read_address_by_id(self, address_id: int) -> model.Address | None:
        return self.__address_da.read_address_by_id(address_id)

    def read_all_addresses(self) -> list[model.Address]:
        return self.__address_da.read_all_addresses()
