import model
from datetime import date
from data_access.base_data_access import BaseDataAccess


class InvoiceDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_new_invoice(self, booking: model.Booking, total_amount: float, issue_date: date) -> model.Invoice:
        if booking is None:
            raise ValueError("Booking is required")
        if total_amount is None:
            raise ValueError("Total amount is required")

        sql = """
        INSERT INTO Invoice (booking_id, issue_date, total_amount)
        VALUES (?, DATE('now'), ?)
        """
        params = (booking.booking_id, total_amount)
        last_row_id, _ = self.execute(sql, params)
        today = date.today()

        return model.Invoice(invoice_id=last_row_id, booking=booking, issue_date=today, total_amount=total_amount)

    def read_invoice_by_id(self, invoice_id: int) -> model.Invoice | None:
        if invoice_id is None:
            raise ValueError("Invoice ID is required")

        sql = """
        SELECT invoice_id, booking_id, issue_date, total_amount
        FROM Invoice WHERE invoice_id = ?
        """
        result = self.fetchone(sql, (invoice_id,))
        if result:
            invoice_id, booking_id, issue_date, total_amount = result
            return model.Invoice(invoice_id, booking_id, issue_date, total_amount)
        return None

    def read_invoices_by_guest(self, guest: model.Guest) -> list[model.Invoice]:
        sql = """
        SELECT i.invoice_id, i.booking_id, i.issue_date, i.total_amount
        FROM Invoice i
        JOIN Booking b ON i.booking_id = b.booking_id
        WHERE b.guest_id = ?
        """
        rows = self.fetchall(sql, (guest.guest_id,))
        return [model.Invoice(*row) for row in rows]
