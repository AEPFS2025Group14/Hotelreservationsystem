import pandas as pd
import model
from data_access.base_data_access import BaseDataAccess


class GuestDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_new_guest(self, first_name: str, last_name: str, email: str, phone: str) -> model.Guest:
        sql = "INSERT INTO Guest (first_name, last_name, email, phone) VALUES (?, ?, ?, ?)"
        last_row_id, _ = self.execute(sql, (first_name, last_name, email, phone))
        return model.Guest(last_row_id, first_name, last_name, email, phone)

    def read_guest_by_id(self, guest_id: int) -> model.Guest | None:
        sql = "SELECT guest_id, first_name, last_name, email, phone FROM Guest WHERE guest_id = ?"
        result = self.fetchone(sql, (guest_id,))
        if result:
            return model.Guest(*result)
        return None

    def read_all_guests(self) -> list[model.Guest]:
        rows = self.fetchall("SELECT * FROM Guest")
        return [model.Guest(*row) for row in rows]

    def read_all_guests_as_df(self) -> pd.DataFrame:
        return pd.read_sql("SELECT * FROM Guest", self._connect(), index_col="guest_id")

    def read_guests_like_name(self, name: str) -> list[model.Guest]:
        sql = "SELECT * FROM Guest WHERE first_name LIKE ? OR last_name LIKE ?"
        params = (f"%{name}%", f"%{name}%")
        rows = self.fetchall(sql, params)
        return [model.Guest(*row) for row in rows]

    def read_guests_like_name_as_df(self, name: str) -> pd.DataFrame:
        sql = "SELECT * FROM Guest WHERE first_name LIKE ? OR last_name LIKE ?"
        params = (f"%{name}%", f"%{name}%")
        return pd.read_sql(sql, self._connect(), params=params, index_col="guest_id")

    def update_guest(self, guest: model.Guest) -> None:
        sql = """
        UPDATE Guest SET first_name = ?, last_name = ?, email = ?, phone = ? WHERE guest_id = ?
        """
        self.execute(sql, (guest.first_name, guest.last_name, guest.email, guest.phone, guest.guest_id))

    def delete_guest(self, guest: model.Guest) -> None:
        self.execute("DELETE FROM Guest WHERE guest_id = ?", (guest.guest_id,))
