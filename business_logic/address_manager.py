import model
import data_access


class AddressManager:
    def __init__(self) -> None:
        self.__address_da = data_access.AddressDataAccess()

    def create_address(self,  street:str, city:str, zip_code:str) -> model.address:
        return self.__address_da.create_new_address()

    def read_address_by_id(self, address_id: int) -> model.Address | None:
        return self.__address_da.read_address_by_id(address_id)

    def read_all_addresses(self) -> list[model.Address]:
        return self.__address_da.read_all_addresses()
