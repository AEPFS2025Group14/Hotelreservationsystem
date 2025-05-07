from datetime import date
from Booking import Booking
from datetime import date

class Invoice:
    def __init__(self, invoice_id :int, issue_date: date, total_amount:float, booking: Booking =None):
        if not invoice_id:
            raise ValueError("Invoice ID is required")
        if not isinstance(invoice_id, int):
            raise ValueError("Invoice ID is not an integer")
        if not issue_date:
            raise ValueError("Issue date is required")
        if not isinstance(issue_date, date):
            raise ValueError("Issue date is not a date")
        if not total_amount:
            raise ValueError("Total amount is required")
        if not isinstance(total_amount, float):
            raise ValueError("Total amount is not a float")

        self.__invoice_id : int = invoice_id
        self.__issue_date : date = issue_date
        self.__total_amount : float = total_amount
        ##if booking is not None:
          ##  booking.add .

    def __repr__(self):
        return (f"Invoice(id={self.__invoice_id!r}, issue_date={self.__issue_date!r},"
                f"total_amount={self.__total_amount!r}, booking={self.__booking!r})")

    @property
    def invoice_id(self) ->int:
        return self.__invoice_id

    @property
    def booking(self) -> Booking:
        return self.__booking

    @booking.setter
    def booking(self, booking : Booking) -> None:
        from Booking import Booking
        if booking is None and not isinstance(booking, Booking):
            raise ValueError("Booking is required")
        if self.__booking is not booking:
            if self.__booking is not None:
                self.__boooking.remove_booking()
            self.booking = booking
            if booking is not None and self not in booking:
                booking.add_booking(self)


    @property
    def issue_date(self) ->date:
        return self.__issue_date

    @issue_date.setter
    def issue_date(self, issue_date : date) -> None:
        if not issue_date:
            raise ValueError("Issue date is required")
        if not isinstance(issue_date, date):
            raise ValueError("Issue date is not a date")
        self.__issue_date = issue_date

    @property
    def total_amount(self) ->float:
        return self.__total_amount
    @total_amount.setter
    def total_amount(self, total_amount : float) -> None:
        if not total_amount:
            raise ValueError("Total amount is required")
        if not isinstance(total_amount, float):
            raise ValueError("Total amount is not a float")
        self.__total_amount = total_amount


