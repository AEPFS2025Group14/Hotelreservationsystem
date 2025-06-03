##Hotel listen geben lassen von Hotelaccess und auch Sterne etc


def validate_search_inputs_1_1(city: str):
    allowed_cities = ["Luzern", "Basel", "Zürich", "Genève", "Bern"]

    if city not in allowed_cities:
        raise ValueError(f"Wir haben leider kein Hotel in der Stadt '{city}'.")



def validate_search_inputs_1_2(city: str, stars: int):
    allowed_cities = ["Luzern", "Basel", "Zürich", "Genève", "Bern"]

    if city not in allowed_cities:
        raise ValueError(f"Wir haben leider kein Hotel in der Stadt '{city}'.")

    if stars != 5:
        raise ValueError("Wir haben leider kein passendes Hotel mit anderen Sternen als 5.")



def validate_search_inputs_1_3(city: str, stars: int, max_guests: int):
    allowed_cities = ["Luzern", "Basel", "Zürich", "Genève", "Bern"]

    if city not in allowed_cities:
        raise ValueError(f"Wir haben leider kein Hotel in der Stadt '{city}'.")

    if 1 > stars > 5:
        raise ValueError("Wir haben leider kein passendes Hotel mit anderen Sternen als 5.")

    if max_guests < 1:
        raise ValueError("Mindestens 1 Person pro Buchung ist erforderlich.")

    if max_guests > 5:
        raise ValueError("Maximal 5 Personen pro Buchung erlaubt.")