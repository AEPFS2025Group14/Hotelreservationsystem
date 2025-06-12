
from IPython.display import HTML, display
from model.invoice import Invoice


class InvoiceRenderer:
    @staticmethod
    def display_invoice(invoice: Invoice) -> None:
        booking = invoice.booking
        guest = booking.guest
        room = booking.room

        html_content = f"""
        <div style="border: 2px solid #444; padding: 20px; max-width: 500px; font-family: Arial;">
            <h2 style="text-align: center; color: #2c3e50;">Hotelrechnung</h2>
            <p><strong>Rechnung-ID:</strong> {invoice.invoice_id}</p>
            <p><strong>Buchung-ID:</strong> {booking.booking_id}</p>
            <p><strong>Ausgestellt am:</strong> {invoice.issue_date}</p>
            <hr>
            <p><strong>Gast:</strong> {guest.first_name} {guest.last_name}</p>
            <p><strong>Zimmernummer:</strong> {room.room_number}</p>
            <p><strong>Check-in:</strong> {booking.check_in_date}</p>
            <p><strong>Check-out:</strong> {booking.check_out_date}</p>
            <p><strong>Preis pro Nacht:</strong> {room.price_per_night:.2f} CHF</p>
            <hr>
            <p><strong>Übernachtungen:</strong> {(booking.check_out_date - booking.check_in_date).days}</p>
            <p><strong>Gesamtbetrag:</strong> <span style="font-size: 1.2em; font-weight: bold;">{invoice.total_amount:.2f} CHF</span></p>
            <hr>
            <p style="text-align: center; color: #2c3e50;">Vielen Dank für Ihren Aufenthalt!</p>
        </div>
        """
        display(HTML(html_content))
