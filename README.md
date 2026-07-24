# expense-tracking-rest-api
RESTful Expense Tracking API built with FastAPI, PostgreSQL, JWT Authentication, and comprehensive API documentation.
# Expense Tracking REST API

A production-style RESTful Expense Tracking API built with **Python**, **FastAPI**, and **PostgreSQL**. The application provides secure user authentication using JWT tokens and allows authenticated users to manage their personal expenses through a clean and modular backend architecture.

## Features

- User registration and login
- JWT-based authentication
- Protected API endpoints
- Expense CRUD (Create, Read, Update, Delete)
- Expense categorization
- PostgreSQL database integration
- Request validation with Pydantic
- Automatic interactive API documentation (Swagger UI)
- Unit testing with pytest

## Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| FastAPI | Backend Framework |
| PostgreSQL | Relational Database |
| SQLAlchemy | ORM |
| JWT | Authentication |
| Pydantic | Data Validation |
| pytest | Testing |
| Postman | API Testing |
| Git & GitHub | Version Control |

## Project Structure

```text
expense-tracking-rest-api/
│
├── app/
│   ├── routers/
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── auth.py
│   └── main.py
│
├── tests/
│
├── requirements.txt
├── README.md
└── .gitignore
```

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /register | Register a new user |
| POST | /login | User login |
| GET | /expenses | Get all expenses |
| POST | /expenses | Add a new expense |
| GET | /expenses/{id} | Get a specific expense |
| PUT | /expenses/{id} | Update an expense |
| DELETE | /expenses/{id} | Delete an expense |

## Authentication

Protected endpoints require a JWT access token.

Example:

```
Authorization: Bearer <your_access_token>
```

## Running the Project

```bash
git clone https://github.com/Fatiha-Mahjabin/expense-tracking-rest-api.git

cd expense-tracking-rest-api

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

## Testing

Run all unit tests using:

```bash
pytest
```

## Future Improvements

- Docker support
- Pagination
- Expense analytics dashboard
- Email verification
- Password reset
- CI/CD pipeline
- Cloud deployment

## Author

**Fatiha Mahjabin**

Applied Mathematics Graduate

Aspiring Software Engineer

Dhaka, Bangladesh
