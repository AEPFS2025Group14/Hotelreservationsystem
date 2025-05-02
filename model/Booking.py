from datetime import date

class Booking:
    def __init__(self, booking_id:int, guest, room, check_in_date:date,check_out_date:date, is_cancelled:bool, total_amount:float ):
        self.__booking_id = booking_id
        self.__guest = guest
        self.__room = room
        self.__check_in_date = check_in_date
        self.__check_out_date = check_out_date
        self.__is_cancelled = is_cancelled
        self.__total_amount = total_amount

    @property
    def booking_id(self):
        return self.__booking_id

    @property
    def guest(self):
        return self.__guest

    @guest.setter
    def guest(self, guest):
        self.__guest = guest

    @property
    def room(self):
        return self.__room

    @room.setter
    def room(self, room):
        self.__room = room

    @property
    def check_in_date(self):
        return self.__check_in_date

    @check_in_date.setter
    def check_in_date(self, check_in_date):
        self.__check_in_date = check_in_date

    @property
    def check_out_date(self):
        return self.__check_out_date

    @check_out_date.setter
    def check_out_date(self, check_out_date):
        self.__check_out_date = check_out_date

    @property
    def is_cancelled(self):
        return self.__is_cancelled

    @is_cancelled.setter
    def is_cancelled(self, is_cancelled):
        self.__is_cancelled = is_cancelled

    @property
    def total_amount(self):
        return self.__total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        self.__total_amount = total_amount

from datetime import timedelta

@property
def duration(self):
    return (self.__check_out_date - self.__check_in_date).days

