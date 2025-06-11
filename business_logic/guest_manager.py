import os
import pandas as pd

import model
import data_access
from model.address import Address
from data_access import AddressDataAccess




class GuestManager:
    def __init__(self):
        self.__guest_da = data_access.GuestDataAccess()

    def create_guest(self, last_name: str, first_name: str, email: str, address:model.Address = None) -> model.Guest:
        return self.__guest_da.create_new_guest(first_name=first_name, last_name=last_name, email=email, address=address)

    def read_guest_by_id(self, guest_id: int) -> model.Guest | None:
        return self.__guest_da.read_guest_by_id(guest_id)

    def read_guest(self, guest_id: int) -> model.Guest:
        return self.__guest_da.read_guest_by_id(guest_id)

    def read_all_guests(self) -> list[model.Guest]:
        return self.__guest_da.read_all_guests()

    def read_all_guests_as_df(self) -> pd.DataFrame:
        return self.__guest_da.read_all_guests_as_df()

    def read_guests_by_similar_name(self, name: str) -> list[model.Guest]:
        return self.__guest_da.read_guests_like_name(name)

    def read_guests_by_similar_name_as_df(self, name: str) -> pd.DataFrame:
        return self.__guest_da.read_guests_like_name_as_df(name)

    def update_guest(self, guest: model.Guest) -> None:
        self.__guest_da.update_guest(guest)

    def delete_guest(self, guest: model.Guest) -> None:
        self.__guest_da.delete_guest(guest)
