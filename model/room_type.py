class RoomType:

    def __init__(self, room_typ_id:int, description:str, max_guests:int):
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


        self.__room_typ_id : int = room_typ_id
        self.__description: str = description
        self.__max_guests : int = max_guests

    def __repr__(self):
        return (f"Roomtype=(id={self.__room_typ_id!r}, description={self.__description!r}, "
                f"max_guests={self.__max_guests!r})")


    @property
    def room_typ_id(self) ->int:
        return self.__room_typ_id

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
        