from model import Invoice
from BaseDataAccess import BaseDataAccess
import sqlite3



class HotelDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)
