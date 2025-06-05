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

# 5. Als Gast möchte ich nach meinem Aufenthalt eine Rechnung erhalten, damit ich einen Zahlungsnachweis habe. Hint: Fügt einen Eintrag in der «Invoice» Tabelle hinzu.

def create_invoice(booking_id: int, issue_date: str, total_amount: float, cursor=None):
    cursor.execute("""
        INSERT INTO Invoice (booking_id, issue_date, total_amount)
        VALUES (?, ?, ?)
    """, (booking_id, issue_date, total_amount))
    conn.commit()
    return f"Invoice for booking {booking_id} on {issue_date} with total {total_amount:.2f} CHF"

# 6. Als Gast möchte ich meine Buchung stornieren, damit ich nicht belastet werde, wenn ich das Zimmer nicht mehr benötige. Hint: Sorgt für die entsprechende Invoice.

def get_invoice_by_booking_id(booking_id: int):
    cursor.execute("""
        SELECT invoice_id, total_amount
        FROM Invoice
        WHERE booking_id = ?
    """, (booking_id,))
    row = cursor.fetchone()
    if row:
        return type('Invoice', (object,), {
            'invoice_id': row[0],
            'total_amount': row[1]
        })()
    return None

def update_invoice_total(invoice_id: int, new_amount: float):
    cursor.execute("""
        UPDATE Invoice
        SET total_amount = ?
        WHERE invoice_id = ?
    """, (new_amount, invoice_id))
    conn.commit()
