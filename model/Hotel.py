from model.Room import Room
from model.Address import Address

class Hotel:
    def __init__(self, hotel_id: int, name:str, stars:int, adresse:Address =None):
        if not hotel_id:
            raise ValueError("hotel_id is required")
        if not isinstance(hotel_id, int):
            raise ValueError("hotel_id must be an integer")
        if not name:
            raise ValueError("name is required")
        if not isinstance(name, str):
            raise ValueError("name must be a string")
        if not stars:
            raise ValueError("stars is required")
        if not isinstance(stars, int):
            raise ValueError("stars must be an integer")

        self.__hotel_id: int  = hotel_id
        self.__name: str = name
        self.__stars: int = stars
        if adresse is not None:
            self.addresse.add_addresse(self)
        self.__rooms: list[Room] = []

    def __repr__(self):
        return f"Hotel(id={self.__hotel_id!r}, name={self.__name!r}, artist={self.__artist!r}, adresse={self.__adresse!r})"

    @property
    def hotel_id(self) -> int:
        return self.__hotel_id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name:str) -> None:
        if not name:
            raise ValueError("name is required")
        if not isinstance(name, str):
            raise ValueError("name must be an string")
        self.__name = name

    @property
    def stars(self) -> int:
        return self.__stars

    @stars.setter
    def stars(self, stars) :
        if not stars:
            raise ValueError("stars is required")
        if not isinstance(stars, int):
            raise ValueError("stars must be an integer")
        self.__stars = stars

    @property
    def adresse(self):
        return self.__adresse
    @adresse.setter
    def adresse(self, adresse):
        self.__adresse = adresse

    @property
    def rooms(self) -> list[Room]:
        return self.__rooms

    @rooms.setter
    def rooms (self, room_id) -> None:
        from model.Room import Room
        return self.rooms.copy()

    def add_room(self, room: Room):
        if not isinstance(room, Room):
            raise ValueError("room must be an instance of Room")
        if room not in self.__rooms:
            self.__rooms.append(room)
            if room.hotel is not self:
                room.hotel = self

    def remove_room(self, room: Room):
        if room in self.__rooms:
            self.__rooms.remove(room)
            if room.hotel is self:
                room.hotel = None



def get_full_address(self):
    return f"{self.__adresse.street}, {self.__adresse.zip_code} {self.__adresse.city}"
