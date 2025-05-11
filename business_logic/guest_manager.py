import os
import pandas as pd

import model
import data_access


class GuestManager:
    def __init__(self):
        self.__guest_da = data_access.GuestDataAccess()

    def create_guest(self, first_name: str, last_name: str, email: str, phone: str) -> model.Guest:
        return self.__guest_da.create_new_guest(first_name, last_name, email, phone)

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
