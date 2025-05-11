import model
import data_access


class InvoiceManager:
    def __init__(self):
        self.__invoice_da = data_access.InvoiceDataAccess()

    def create_invoice(self, booking: model.Booking, total_amount: float) -> model.Invoice:
        return self.__invoice_da.create_new_invoice(booking, total_amount)

    def read_invoice(self, invoice_id: int) -> model.Invoice:
        return self.__invoice_da.read_invoice_by_id(invoice_id)

    def read_invoices_by_guest(self, guest: model.Guest) -> list[model.Invoice]:
        return self.__invoice_da.read_invoices_by_guest(guest)
