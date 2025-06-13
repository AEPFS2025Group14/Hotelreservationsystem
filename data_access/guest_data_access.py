import pandas as pd

import data_access
import model
from data_access.base_data_access import BaseDataAccess


class GuestDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)
        self.__address_da = data_access.AddressDataAccess(db_path)

    def create_new_guest(self, first_name: str, last_name: str, email: str, address: model.Address = None) -> model.Guest:
        address_id = None
        if address:
            address_id = self.__address_da.create_new_address(address)
        sql = """INSERT INTO Guest (first_name, last_name, email, address_id) VALUES (?, ?, ?, ?)"""
        last_row_id, _ = self.execute(sql, (first_name, last_name, email, address_id))
        return model.Guest(last_row_id, first_name, last_name, email, address_id)

    def read_guest_by_id(self, guest_id: int) -> model.Guest | None:
        sql = """
        SELECT guest_id, first_name, last_name, email, address_id FROM Guest WHERE guest_id = ?"""
        params = (guest_id,)
        result = self.fetchone(sql, params)

        if result:
            guest_id, first_name, last_name, email, address_id = result
            if email is None:
                email = ""
            address = self.__address_da.read_address_by_id(address_id) if address_id else None
            return model.Guest(guest_id, first_name, last_name, email, address)
        return None

    ##Zusätzliche Funktionen welche nützliche sein können aber nicht gefragt waren in den Userstories.
    def update_guest(self, guest: model.Guest) -> None:
        sql = """
        UPDATE Guest SET first_name = ?, last_name = ?, email = ? WHERE guest_id = ?
        """
        self.execute(sql, (guest.first_name, guest.last_name, guest.email, guest.guest_id))

