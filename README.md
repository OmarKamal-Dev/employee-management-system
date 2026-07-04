# Employee Management & Log System

A simple Python-based system for managing employee records (add, update, delete, search, list), with a basic login system using a username and password.

> ⚠️ **Note:** This is a beginner project built while I'm still learning Python, so there might be some rough edges or small mistakes. Feedback and suggestions are more than welcome! 🙌

## Features

- Login with limited attempts (3 tries for the password)
- Add a new employee
- Update an existing employee's data
- Delete an employee (with confirmation before deleting)
- Search for an employee by name
- Display a list of all employees
- Data stored in JSON files (JSON Lines format)

## Project Structure

```
Employee Management & Log System/
│
├── main.py        # Entry point and menus
├── dp.py          # Data layer (reading/writing JSON)
├── session.py     # Stores the current session state
├── utils.py       # Helper functions (printing, input validation, login)
├── Employee.json  # Employee data file
└── Users.json     # User data file (username and password)
```

## How to Run

1. Make sure Python is installed (3.12+ recommended, since the code uses nested f-strings).
2. Open a terminal in the project folder.
3. Run:

```bash
python main.py
```

4. Log in using credentials from `Users.json` (example: `omar` / `1234`).

## Built With

- Python (Standard Library only — no external dependencies)
- JSON for data storage

## To-Do

- [ ] Validate input (e.g., make sure age and salary are numbers)
- [ ] Hash passwords instead of storing them as plain text
- [ ] Prevent duplicate employee names
- [ ] Add error handling for file reading/writing

## Final Note

This project is part of my journey learning Python. Any feedback or pull requests would mean a lot to me 🙏
