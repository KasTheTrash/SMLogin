# Secure Login System

## Overview
A secure login interface built with Python/Tkinter that provides user authentication for the StoreManager Pro system. The application features a modern GUI, secure password handling with bcrypt encryption, and PostgreSQL database integration.

## Features
- Secure password verification using bcrypt
- PostgreSQL database integration
- Modern Tkinter GUI interface
- Automatic database table creation
- Case-insensitive username handling
- Tab-order navigation support
- Automatic redirection to main application after successful login
- Error handling and user feedback
- Thread-safe application launching

## Technical Stack
- Python 3.x
- Tkinter for GUI
- PostgreSQL for database
- psycopg2 for database connectivity
- bcrypt for password verification
- Threading for application launching

## Prerequisites
- Python 3.x
- PostgreSQL Server
- Required Python packages:
  ```
  psycopg2
  bcrypt
  ```

## Database Configuration
The application requires a PostgreSQL database with the following configuration:
```
Database Name: StoreManager
Host: localhost
Port: 5432
User: postgres
```

### Database Schema
The application automatically creates the required table if it doesn't exist:
```sql
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(60) NOT NULL
);
```

## Installation
1. Clone the repository
   ```bash
   git clone https://github.com/KasTheTrash/login-system.git
   ```

2. Install required packages
   ```bash
   pip install psycopg2 bcrypt
   ```

3. Ensure PostgreSQL server is running

4. Run the application
   ```bash
   python login.py
   ```

## Security Features
- Password verification using bcrypt
- Case-insensitive username comparison
- Secure database connections
- Password masking in the UI
- Automatic window cleanup after login

## Directory Structure
```
├── login.py
├── assets/
│   └── frame0/
│       ├── button_1.png
│       ├── entry_1.png
│       └── entry_2.png
└── main.py (required for successful login)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Author
[KasTheTrash]

## Notes
- The system requires `main.py` to be present in the same directory for successful login redirection
- Assets folder must contain required GUI elements
- Database credentials should be properly configured before use
