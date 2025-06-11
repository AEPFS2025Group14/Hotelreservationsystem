from datetime import date
from model.address import Address
import model
from datetime import datetime, date
import business_logic



class Validation_functions:


## Hotel
    @staticmethod
    def validate_city(city: str):
        if not city or not city.strip():
            raise ValueError("Stadt darf nicht leer sein.")

    @staticmethod
    def normalize_city(city: str) -> str:
        Validation_functions.validate_city(city)
        return city.strip().upper()

    @staticmethod
    def validate_stars(stars: int):
        if not isinstance(stars, int) or stars < 1 or stars > 5:
            raise ValueError("Sterne müssen eine ganze Zahl zwischen 1 und 5 sein.")

    @staticmethod
    def validate_zip_code(zip_code: str):
        if not zip_code or not zip_code.isdigit():
            raise ValueError("PLZ muss eine gültige Zahl sein.")


    @staticmethod
    def validate_max_guests(max_guests: int):
        if not isinstance(max_guests, int) or max_guests < 1 or max_guests > 6:
            raise ValueError("Die maximale Gästeanzahl muss zwischen 1 und 6 liegen.")

    @staticmethod
    def validate_street(street: str):
        if not street or not street.strip():
            raise ValueError("Straße darf nicht leer sein.")

    @staticmethod
    def validate_name(name: str):
            if not name or not name.strip():
                raise ValueError("Hotelname darf nicht leer sein.")
    @staticmethod
    def validate_address(address: Address):
        if not address or not address.city or not address.street or not address.zip_code:
            raise ValueError("Adresse ist unvollständig oder fehlt.")

    ##Booking
    @staticmethod
    def validate_booking_dates(check_in_date: date, check_out_date: date) -> None:
        if check_in_date < date.today():
            raise ValueError("Check-in-Datum darf nicht in der Vergangenheit liegen.")
        if check_in_date >= check_out_date:
            raise ValueError("Check-out-Datum muss vor dem Check-out-Datum liegen.")


    @staticmethod
    def parse_and_validate_dates(check_in_date: str, check_out_date: str) -> tuple[date, date]:
        check_in = Validation_functions.parse_date_string(check_in_date)
        check_out = Validation_functions.parse_date_string(check_out_date)
        Validation_functions.validate_booking_dates(check_in, check_out)
        return check_in, check_out


    @staticmethod
    def parse_date_string(date_str: str) -> date:
        if isinstance(date_str, date):
            return date_str
        try:
            return datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError(f"Ungültiges Datum: '{date_str}'. Format muss YYYY-MM-DD sein.")

    ##Guest
    def validate_guest_data(first_name: str, last_name: str, email: str) -> None:
        if not first_name or not last_name:
            raise ValueError("Vor- und Nachname dürfen nicht leer sein.")
        if "@" not in email or "." not in email:
            raise ValueError("Ungültige E-Mail-Adresse.")


