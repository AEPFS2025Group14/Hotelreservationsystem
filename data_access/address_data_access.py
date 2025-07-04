import model
from data_access.base_data_access import BaseDataAccess


class AddressDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_new_address(self,  street:str, city:str, zip_code:str) -> model.Address:
        if street is None:
            raise ValueError("street is required")
        if city is None:
            raise ValueError("city is required")
        if zip_code is None:
            raise ValueError("zip_code is required")
        sql = """ 
        INSERT INTO Address (street, city, zip_code) VALUES (?, ?, ?)
        """

        params = (street, city, zip_code)
        last_row_id, row_count = self.execute(sql, params)
        return model.Address(address_id=last_row_id, street=street, city=city, zip_code=zip_code)

    def read_address_by_id(self, address_id: int) -> model.Address | None:
        sql = """
        SELECT address_id, street, city, zip_code FROM Address WHERE address_id = ?
        """
        params = (address_id,)
        result = self.fetchone(sql, params)
        if result:
            address_id, street, city, zip_code = result
            return model.Address(address_id, street, city, zip_code)
        else:
            return None

