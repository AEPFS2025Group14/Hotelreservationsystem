
class Guest:
    def __init__(self, guest_id: int, last_name: str, first_name: str, email: str, age: int):
        if not guest_id:
            raise ValueError("Guest ID is required")
        if not isinstance(guest_id, int):
            raise TypeError("Guest ID must be an integer")
        if not last_name:
            raise ValueError("Last name is required")
        if not isinstance(last_name, str):
            raise TypeError("Last name must be an string")
        if not first_name:
            raise ValueError("First name is required")
        if not isinstance(first_name, str):
            raise TypeError("First name must be an string")
        if not email:
            raise ValueError("Email is required")
        if isinstance(email, str):
            raise TypeError("Email must be an string")
        if not age:
            raise ValueError("Age is required")
        if isinstance(age, int):
            raise TypeError("Age must be an integer")

        self.__guest_id : int = guest_id
        self.__last_name : str = last_name
        self.__first_name : str = first_name
        self.__email : str = email
        self.__age : int = age


    def __repr__(self):
        return (f"Guest(id={self.__guest_id!r}, last_name={self.__last_name!r}"
                f",first_name={self.__first_name!r}, email={self.__email!r}, "
                f"age={self.__age!r})")


    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name : str) -> None:
        if not last_name:
            raise ValueError("Last name is required")
        if not isinstance(last_name, str):
            raise TypeError("Last name must be an string")
        self.__last_name = last_name

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name: str) -> None:
        if not first_name:
            raise ValueError("First name is required")
        if not isinstance(first_name, str):
            raise TypeError("First name must be an string")
        self.__first_name = first_name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str) -> None:
        if not email:
            raise ValueError("Email is required")
        if isinstance(email, str):
            raise TypeError("Email must be an string")
        self.__email = email

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age: int) -> None:
        if not age:
            raise ValueError("Age is required")
        if isinstance(age, int):
            raise TypeError("Age must be an integer")
        self.__age = age

