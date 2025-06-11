import data_access
import model
from model.address import Address
from business_logic.validation_functions import Validation_functions


class GuestManager:
    def __init__(self):
        self.__guest_da = data_access.GuestDataAccess()

    def create_guest(self, first_name: str, last_name: str, email: str, address: Address = None) -> model.Guest:
        Validation_functions.validate_guest_data(first_name, last_name, email)
        return self.__guest_da.create_new_guest(
            first_name=first_name.strip(),
            last_name=last_name.strip(),
            email=email.strip(),
            address=address
        )

    def read_guest_by_id(self, guest_id: int) -> model.Guest | None:
        return self.__guest_da.read_guest_by_id(guest_id)

    ##Zusätzlich
    def update_guest(self, guest: model.Guest) -> None:
        if not guest:
            raise ValueError("Ungültiges Guest-Objekt.")
        Validation_functions.validate_guest_data(guest.first_name, guest.last_name, guest.email)
        self.__guest_da.update_guest(guest)
