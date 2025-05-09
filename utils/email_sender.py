import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_booking_email(to_email, guest_name, hotel_name, check_in, check_out, total_amount):
    sender_email = "your@email.com"
    password = "your-email-password"  # ⚠️ Achtung: Für Tests ggf. App-Passwort verwenden

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = "Your Hotel Booking Confirmation"

    body = f"""
    Hello {guest_name},

    Your booking at {hotel_name} from {check_in} to {check_out} is confirmed.
    Total: {total_amount:.2f} CHF

    Thank you for your reservation!
    """
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    text = msg.as_string()
    server.sendmail(sender_email, to_email, text)
    server.quit()
