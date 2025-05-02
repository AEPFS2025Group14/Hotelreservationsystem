from Mensch import Mensch
class Guest(Mensch):
    def __init__(self, guest_id:int, last_name:str, first_name:str, alter:int, email:str):
        super().__init__(last_name, first_name, email, alter)
        self.__guest_id = guest_id

    @property
    def guest_id(self):
        return self.__guest_id  # Getter for guest_

Gast1 = Guest(1, "Muster", "Max", 21, "max@muster")
print(Gast1.guest_id)

def get_full_name(self):
    return f"{self.first_name} {self.last_name}"
