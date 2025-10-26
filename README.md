# SmartBank - Modular Banking Backend

## Tech Stack
- **Backend Framework:** Django, Django REST Framework (DRF)  
- **Database:** SQLite (default, lightweight for development)  
- **Authentication:** JWT via `djangorestframework-simplejwt`  
- **Rate Limiting:** SlowAPI  
- **Testing:** PyTest + DRF test client  
- **Security:** Password hashing, role-based access control, input validation  

---

## Project Structure

## Project Structure

SmartBank/
│
├── smartbank/        # Django project root (settings, urls, wsgi)
│
└── banking/          # Single app for authentication and account creation
    ├── models.py         # User and Account models
    ├── serializers.py    # Data validation for registration/login and account creation
    ├── views.py          # Endpoints: register, login, create account
    ├── permissions.py    # Role-based access control
    ├── urls.py           # API routes
    ├── tests.py          # Unit and integration tests
    └── utils.py          # Helper functions (optional)




## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/register/` | POST | Register a new user |
| `/login/` | POST | Authenticate user, return JWT token |
| `/create-account/` | POST | Create a new bank account (customer only) |
