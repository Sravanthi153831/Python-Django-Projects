# Employee Management System

A simple Employee Management System built using Python, Flask, SQLite, and Flask REST API.

## Technologies Used

- Python
- Flask
- SQLite
- Flask REST API

## Features

- View all employees
- Add a new employee
- Update employee details
- Delete an employee
- Search employees
- Store employee data using SQLite
- RESTful API operations

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/employees` | Get all employees |
| POST | `/employees` | Add a new employee |
| PUT | `/employees/<id>` | Update an employee |
| DELETE | `/employees/<id>` | Delete an employee |

## Example Employee Data

```json
{
    "id": 106,
    "name": "Kiran",
    "department": "Software",
    "salary": 70000
}


