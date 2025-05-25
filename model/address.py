class Address:
    def __init__(self, address_id: int, street:str, city:str, zip_code:str):
        if not address_id:
            raise ValueError("address_id is required")
        if not isinstance(address_id, int):
            raise ValueError("address_id must be an integer")
        if not street:
            raise ValueError("stress is required")
        if not isinstance(street, str):
            raise ValueError("street must be an string")
        if not city:
            raise ValueError("city is required")
        if not isinstance(city, str):
            raise ValueError("city must be a string")
        if not zip_code:
            raise ValueError("zip code is required")
        if not isinstance(zip_code, str):
            raise ValueError("zip code must be a string")

        self.__address_id: int = address_id
        self.__street: str = street
        self.__city: str = city
        self.zip_code: str = zip_code

    def __repr__(self):
        return (f"Address(id={self.__address_id!r}, "
                f"street={self.__street!r}, city={self.__city!r}, zip_code={self.__zip_code!r})")

    @property
    def address_id(self) -> int:
        return self.__address_id

    @property
    def street(self) -> str:
        return self.__street

    @street.setter
    def street(self, street:str) -> None:
        self.__street = street
        if not street:
            raise ValueError("street is required")
        if not isinstance(street, str):
            raise ValueError("street must be an string")
        self.__street = street

    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, city:str) -> None:
        self.__city = city
        if not city:
            raise ValueError("city is required")
        if not isinstance(city, str):
            raise ValueError("city must be an string")
        self.__city = city

    @property
    def zip_code(self) -> str:
        return self.__zip_code
    @zip_code.setter
    def zip_code(self, zip_code:str) -> None:
        self.__zip_code = zip_code
        if not zip_code:
            raise ValueError("zip code is required")
        if not isinstance(zip_code, str):
            raise ValueError("zip code must be an string")
        self.__zip_code = zip_code


