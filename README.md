# Assignment

## Backend
Run the Django server in the project root:
```bash
python manage.py runserver
```
## Frontend
Navigate to frontend folder:
```bash
cd frontend
```
Install dependencies and start the development server:
```bash
npm install
npm run dev
```

## Overview
Everything in the assignment is working except for the ability to filter by date (I haven’t had enough time to implement that).
I have not used Python as a backend technology in a professional environment (aside from a smaller project using FastAPI, Jinja,
and some machine learning projects at university),
so I followed the Django REST Framework documentation and used help from ChatGPT to better understand Django’s architecture.

# Assumptions & decisions

I tried to follow the assignment document with simplicity in mind. I did not include unnecessary abstraction layers in the codebase.
I created a basic fetch service, a couple of interfaces, and a few UI components. I did include some of the ESLint rules I prefer to use.

The functionality assumes that each order must include at least one pickup and one delivery waypoint.
It also assumes that the order_number is set by the user, as requested in the assignment document.

Thank you for taking the time to review my assignment.
