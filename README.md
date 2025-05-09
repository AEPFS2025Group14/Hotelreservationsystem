# AEP Hotel Reservation System – Reference Implementation

This project implements a hotel reservation system as part of the FHNW module *Application Development with Python* (AEP, FS2025).  
It demonstrates how to combine Python, SQLite, and basic data modeling to implement user stories through real database queries.

## Scenario

The system allows users (guests and admins) to interact with hotel data, view available rooms, make bookings, generate invoices, and more.

## Tools & Technologies

- Python 3.10+
- SQLite
- pandas
- matplotlib (for visualization)
- fpdf (PDF booking confirmation)
- Jupyter Notebook (for data insights and optional analytics)

## Project Structure



## Implemented User Stories

### Mandatory user stories:
- View hotels by city
- Filter hotels by stars, guests, and availability
- View available rooms with details and price
- Book a room
- Generate an invoice for a booking
- Cancel a booking
- Admin: Add, update, or delete hotels

### Optional user stories:
- Generate a PDF booking confirmation
- Leave a hotel review
- Show average guest age
- Visualize room type popularity (bar chart)
- Revenue overview by month (line chart)

---

## Notebook Visualizations

The notebook `Hotelreservation.ipynb` includes:

- Popular room types (bar chart)
- Monthly revenue trend (line chart)
- Guest demographics (age average)

---

## How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt

2. Run the CLI interface:
 ```bash
python main.py


