class Roomtype:

    def __init__(self, room_typ_id:int, description:str, max_guests:int, price_per_night:float):
        if not room_typ_id:
            raise ValueError("Roomtype id is required")
        if not isinstance(room_typ_id, int):
            raise ValueError("Roomtype id must be an integer")
        if not description:
            raise ValueError("Roomtype description is required")
        if not isinstance(description, str):
            raise ValueError("Roomtype description must be a string")
        if not max_guests:
            raise ValueError("Roomtype max_guests is required")
        if not isinstance(max_guests, int):
            raise ValueError("Roomtype max_guests must be an integer")
        if not price_per_night:
            raise ValueError("Roomtype price_per_night is required")
        if not isinstance(price_per_night, float):
            raise ValueError("Roomtype price_per_night must be a float")


        self.__room_typ : int = room_typ_id
        self.__description: str = description
        self.__max_guests : int = max_guests
        self.__price_per_night : float = price_per_night

    def __repr__(self):
        return (f"Roomtype=(id={self.__room_typ_id!r}, description={self.__description!r}, "
                f"max_guests={self.__max_guests!r})")


    @property
    def room_type_id(self) ->int:
        return self.__room_typ

    @property
    def description(self) ->str:
        return self.__description

    @description.setter
    def description(self, description: str) -> None:
        if not description:
            raise ValueError("Roomtype description is required")
        if not isinstance(description, str):
            raise ValueError("Roomtype description must be a string")
        self.__description = description

    @property
    def max_guests(self) -> int:
        return self.__max_guests

    @max_guests.setter
    def max_guests(self, max_guests: int) -> None:
        if not max_guests:
            raise ValueError("Roomtype max_guests is required")
        if not isinstance(max_guests, int):
            raise ValueError("Roomtype max_guests must be an integer")
        self.__max_guests = max_guests

    @property
    def price_per_night(self):
        return self.__price_per_night


    @price_per_night.setter
    def price_per_night(self, price_per_night: float) -> None:
        if not price_per_night:
            raise ValueError("Roomtype price_per_night is required")
        if not isinstance(price_per_night, float):
            raise ValueError("Roomtype price_per_night must be a float")
        return self.__price_per_night
