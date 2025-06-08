import model
import data_access
from datetime import date


class InvoiceManager:
    def __init__(self):
        self.__invoice_da = data_access.InvoiceDataAccess()

    def create_new_invoice(self, booking: model.Booking, total_amount: float, issue_date:date) -> model.Invoice:
        return self.__invoice_da.create_new_invoice(booking=booking, total_amount=total_amount, issue_date=issue_date)

    def read_invoice(self, invoice_id: int) -> model.Invoice:
        return self.__invoice_da.read_invoice_by_id(invoice_id)

    def read_invoices_by_guest(self, guest: model.Guest) -> list[model.Invoice]:
        return self.__invoice_da.read_invoices_by_guest(guest)


    def create_invoice(booking_id: int, issue_date: str, total_amount: float, cursor=None):
        pass

    def read_invoice_by_id(self, invoice_id: int) -> model.Invoice | None:
        return self.__invoice_da.read_invoice_by_id(invoice_id)

    def update_invoice_total(invoice_id: int, new_amount: float):
        pass