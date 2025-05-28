##ABFRAGEN AB 1.4


query: """ 
        SELECT hotel_id, name, stars, Address.address_id, street, city, zip_code FROM Hotel
        JOIN Address ON Address.address_id = Hotel.address_id
        WHERE Address.city = ?
        """

