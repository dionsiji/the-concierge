# The Concierge 🍽️

The Concierge is a luxury restaurant reservation web application designed to simulate the booking experience of a high-end dining establishment. The system allows users to reserve tables, select dining times, and view real-time seat availability.

The goal of the project is to replicate the reservation experience offered by premium restaurants while demonstrating backend system design, database integration, and reservation management logic.

---

## Features

- Interactive table reservation system
- Table selection based on number of guests
- Reservation time scheduling
- Visualization of booked and available tables
- Reservation conflict prevention
- User-friendly reservation interface
- Structured backend logic for managing bookings

---

## Tech Stack

Backend  
- Python  
- Django  

Frontend  
- HTML  
- CSS  
- JavaScript  

Database  
- SQLite (default Django database)

---

## System Overview

The application allows customers to:

1. Select a date and reservation time
2. Choose a table based on seating capacity
3. View tables that are already reserved
4. Confirm their reservation

The backend handles reservation validation and ensures that tables cannot be double-booked.

---

## Project Structure

```
the-concierge/
│
├── concierge/        # Django project configuration
├── reservations/     # Reservation system app
├── templates/        # HTML templates
├── static/           # CSS / JavaScript / assets
├── db.sqlite3
└── manage.py
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/the-concierge.git
cd the-concierge
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

Windows

```bash
venv\Scripts\activate
```

Mac/Linux

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Open the app in your browser:

```
http://127.0.0.1:8000
```

---

## Future Improvements

- User authentication and profile management
- Admin dashboard for reservation management
- Email confirmation for reservations
- Real-time table availability updates
- Integration with external restaurant management systems

---

## Author

Dion Siji  
MCA Student | Python & AI Enthusiast | Backend Development
