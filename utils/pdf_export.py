from fpdf import FPDF


def create_booking_confirmation(guest_name, hotel_name, check_in, check_out, total_amount):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Booking Confirmation", ln=True, align='C')
    pdf.cell(200, 10, txt=f"Guest: {guest_name}", ln=True)
    pdf.cell(200, 10, txt=f"Hotel: {hotel_name}", ln=True)
    pdf.cell(200, 10, txt=f"Check-in: {check_in}", ln=True)
    pdf.cell(200, 10, txt=f"Check-out: {check_out}", ln=True)
    pdf.cell(200, 10, txt=f"Total: {total_amount:.2f} CHF", ln=True)

    pdf.output("booking_confirmation.pdf")
