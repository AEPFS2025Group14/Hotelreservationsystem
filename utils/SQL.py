##ABFRAGEN AB 1.4


query: """ 
        SELECT hotel_id, name, stars, Address.address_id, street, city, zip_code FROM Hotel
        JOIN Address ON Address.address_id = Hotel.address_id
        WHERE Address.city = ?
        """

#3.1

INSERT INTO Hotel (hotel_id, name, stars, address_id)
VALUES (?, ?, ?, ?);

#3.2

DELETE FROM Hotel
WHERE hotel_id = ?;

#3.3

UPDATE Hotel
SET name = ?, stars = ?, address_id = ?
WHERE hotel_id = ?;

#4

INSERT INTO Booking (booking_id, guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount)
VALUES (?, ?, ?, ?, ?, 0, ?);

#5

INSERT INTO Invoice (invoice_id, booking_id, issue_date, total_amount)
VALUES (?, ?, DATE('now'), ?);

#6

UPDATE Booking
SET is_cancelled = 1, total_amount = 0
WHERE booking_id = ?;

-- und optional auch:
INSERT INTO Invoice (invoice_id, booking_id, issue_date, total_amount)
VALUES (?, ?, DATE('now'), 0.00);

#7

SELECT
    r.room_id,
    r.room_number,
    r.price_per_night *
        CASE
            WHEN ? BETWEEN '2025-07-01' AND '2025-08-31' THEN 1.2 -- Hochsaison
            WHEN ? BETWEEN '2025-12-20' AND '2026-01-05' THEN 1.3 -- Weihnachten/Neujahr
            ELSE 1.0 -- Normaltarif
        END AS dynamic_price
FROM
    Room r;

#8

SELECT
    b.booking_id,
    g.first_name || ' ' || g.last_name AS guest_name,
    h.name AS hotel_name,
    r.room_number,
    b.check_in_date,
    b.check_out_date,
    b.is_cancelled,
    b.total_amount
FROM
    Booking b
JOIN Guest g ON b.guest_id = g.guest_id
JOIN Room r ON b.room_id = r.room_id
JOIN Hotel h ON r.hotel_id = h.hotel_id;

#9

SELECT
    r.room_id,
    r.room_number,
    h.name AS hotel_name,
    f.facility_name
FROM
    Room r
JOIN Hotel h ON r.hotel_id = h.hotel_id
JOIN Room_Facilities rf ON r.room_id = rf.room_id
JOIN Facilities f ON rf.facility_id = f.facility_id
ORDER BY
    r.room_id, f.facility_name;

#10
# a) Zimmertyp aktualisieren

UPDATE Room_Type
SET description = ?, max_guests = ?
WHERE type_id = ?;

# b) Einrichtung aktualisieren

UPDATE Facilities
SET facility_name = ?
WHERE facility_id = ?;

# c) Preis pro Nacht für ein Zimmer aktualisieren

UPDATE Room
SET price_per_night = ?
WHERE room_id = ?;

# SQL Abfragen zu User Stories mit DB-Schemaänderung

#1
# Schemaänderung
ALTER TABLE Guest ADD COLUMN phone TEXT;

#Update-Abfrage
UPDATE Guest
SET phone = ?
WHERE guest_id = ?;

#2
SELECT
    b.booking_id,
    h.name AS hotel_name,
    r.room_number,
    b.check_in_date,
    b.check_out_date,
    b.total_amount,
    b.is_cancelled
FROM
    Booking b
JOIN Room r ON b.room_id = r.room_id
JOIN Hotel h ON r.hotel_id = h.hotel_id
WHERE
    b.guest_id = ?
ORDER BY
    b.check_in_date DESC;

#2.1
# neu erstellen
INSERT INTO Booking (booking_id, guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount)
VALUES (?, ?, ?, ?, ?, 0, ?);

# ändern / aktualisieren
UPDATE Booking
SET check_in_date = ?, check_out_date = ?, room_id = ?, total_amount = ?
WHERE booking_id = ? AND guest_id = ?;

# stornieren
UPDATE Booking
SET is_cancelled = 1, total_amount = 0
WHERE booking_id = ? AND guest_id = ?;

# löschen
DELETE FROM Booking
WHERE booking_id = ? AND guest_id = ?;

#3
# neue Tabelle notwendig
CREATE TABLE Review (
    review_id INTEGER PRIMARY KEY,
    guest_id INTEGER NOT NULL,
    hotel_id INTEGER NOT NULL,
    rating INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
    comment TEXT,
    review_date DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY (guest_id) REFERENCES Guest(guest_id),
    FOREIGN KEY (hotel_id) REFERENCES Hotel(hotel_id)
);

# einfügen einer Bewertung
INSERT INTO Review (review_id, guest_id, hotel_id, rating, comment)
VALUES (?, ?, ?, ?, ?);

#4

SELECT
    r.rating,
    r.comment,
    g.first_name || ' ' || g.last_name AS guest_name,
    r.review_date
FROM
    Review r
JOIN Guest g ON r.guest_id = g.guest_id
WHERE
    r.hotel_id = ?;

#5

# neue Tabelle
CREATE TABLE Loyalty_Points (
    guest_id INTEGER PRIMARY KEY,
    points INTEGER DEFAULT 0,
    FOREIGN KEY (guest_id) REFERENCES Guest(guest_id)
);

# Regel für häufige Gäste
SELECT
    guest_id,
    COUNT(*) AS total_bookings
FROM
    Booking
WHERE
    is_cancelled = 0
GROUP BY
    guest_id
HAVING
    COUNT(*) >= 3;

#Punkte eintragen (nach Aufenthalt)
UPDATE Loyalty_Points
SET points = points + ?
WHERE guest_id = ?;

#6
# neue Tabelle
CREATE TABLE Payment (
    payment_id INTEGER PRIMARY KEY,
    booking_id INTEGER NOT NULL,
    method TEXT NOT NULL, -- z. B. 'Credit Card', 'Twint', 'PayPal'
    paid_amount REAL NOT NULL,
    payment_date DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY (booking_id) REFERENCES Booking(booking_id)
);

# Bezahlvorgang
INSERT INTO Payment (payment_id, booking_id, method, paid_amount)
VALUES (?, ?, ?, ?);

#SQL Abfragen zu Datenvisualisierung
#1

SELECT
    rt.description AS room_type,
    COUNT(b.booking_id) AS booking_count
FROM
    Booking b
JOIN Room r ON b.room_id = r.room_id
JOIN Room_Type rt ON r.type_id = rt.type_id
WHERE
    b.is_cancelled = 0
GROUP BY
    rt.description
ORDER BY
    booking_count DESC;

#2
# Vorbereitend: Neue Spalte birthdate zur Guest-Tabelle hinzufügen
ALTER TABLE Guest ADD COLUMN birthdate DATE;

#Gäste nach Altersspanne gruppieren
SELECT
    CASE
        WHEN (strftime('%Y', 'now') - strftime('%Y', birthdate)) < 20 THEN 'Unter 20'
        WHEN (strftime('%Y', 'now') - strftime('%Y', birthdate)) BETWEEN 20 AND 29 THEN '20-29'
        WHEN (strftime('%Y', 'now') - strftime('%Y', birthdate)) BETWEEN 30 AND 39 THEN '30-39'
        WHEN (strftime('%Y', 'now') - strftime('%Y', birthdate)) BETWEEN 40 AND 49 THEN '40-49'
        ELSE '50+'
    END AS age_group,
    COUNT(*) AS guest_count
FROM
    Guest
WHERE birthdate IS NOT NULL
GROUP BY
    age_group
ORDER BY
    guest_count DESC;

#Optional – wiederkehrende Gäste identifizieren
SELECT
    g.guest_id,
    g.first_name || ' ' || g.last_name AS name,
    COUNT(b.booking_id) AS bookings
FROM
    Guest g
JOIN Booking b ON g.guest_id = b.guest_id
WHERE
    b.is_cancelled = 0
GROUP BY
    g.guest_id
HAVING
    COUNT(b.booking_id) >= 2
ORDER BY
    bookings DESC;

#SQL Abfragen zu den Optionalen User Stories

#1.1

SELECT
    h.name AS hotel_name,
    SUM(i.total_amount) AS total_revenue
FROM
    Invoice i
JOIN Booking b ON i.booking_id = b.booking_id
JOIN Room r ON b.room_id = r.room_id
JOIN Hotel h ON r.hotel_id = h.hotel_id
WHERE
    i.issue_date BETWEEN ? AND ?
GROUP BY
    h.hotel_id;

#1.2

SELECT
    strftime('%Y-%m', i.issue_date) AS month,
    SUM(i.total_amount) AS monthly_revenue
FROM
    Invoice i
WHERE
    i.total_amount > 0
GROUP BY
    month
ORDER BY
    month;

#2

SELECT
    b.booking_id,
    g.first_name || ' ' || g.last_name AS guest_name,
    h.name AS hotel_name,
    r.room_number,
    rt.description AS room_type,
    b.check_in_date,
    b.check_out_date,
    b.total_amount
FROM
    Booking b
JOIN Guest g ON b.guest_id = g.guest_id
JOIN Room r ON b.room_id = r.room_id
JOIN Room_Type rt ON r.type_id = rt.type_id
JOIN Hotel h ON r.hotel_id = h.hotel_id
WHERE
    b.booking_id = ?;

#3
#Voraussetzung: Neue Spalten latitude, longitude in der Address-Tabelle:
ALTER TABLE Address ADD COLUMN latitude REAL;
ALTER TABLE Address ADD COLUMN longitude REAL;

#Abfrage für Geodaten des gebuchten Hotels:
SELECT
    a.city,
    a.street,
    a.latitude,
    a.longitude
FROM
    Booking b
JOIN Room r ON b.room_id = r.room_id
JOIN Hotel h ON r.hotel_id = h.hotel_id
JOIN Address a ON h.address_id = a.address_id
WHERE
    b.booking_id = ?;

#4
#Kein SQL notwendig – stattdessen: Nutze die SQL aus 2. für Buchungsdetails und verwende:

