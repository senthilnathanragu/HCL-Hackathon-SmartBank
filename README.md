# SmartBank - Modular Banking Backend 

# Primary Use case - Account creation

## Tech Stack
- **Backend Framework:** Django, Django REST Framework (DRF)  
- **Database:** SQLite (default, lightweight for development)  
- **Authentication:** JWT via `djangorestframework-simplejwt`  
- **Rate Limiting:** SlowAPI  
- **Testing:** PyTest + DRF test client  
- **Security:** Password hashing, role-based access control, input validation  

---

## Features Implemented
- **User Registration & Login:** Customers can register and login to the system.
- **Role-Based Access Control (RBAC):** Only users with the correct role (Customer, Admin, Auditor) can access certain endpoints.
- **Account Creation:** Customers can create accounts (Savings, Current, FD) with unique 12-digit account numbers.
- **JWT Authentication:** Secure stateless API access using access and refresh tokens.
- **Password Security:** Passwords are hashed using Bcrypt before storing.
- **Input Validation & Sanitization:** Ensures all API input data is validated.

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/register/` | POST | Register a new user |
| `/login/` | POST | Authenticate user, return JWT token |
| `/create-account/` | POST | Create a new bank account (customer only) |
| `/admin-dashboard/` | GET | Access admin dashboard (admin only) |
| `/audit-logs/` | GET | View audit logs (auditor only) |


## Application Overview

1. **User Registration**  
Customers submit their personal details (username, email, password, etc.).  
The system validates inputs and securely stores user profiles in the database.

2. **Account Creation**  
Customers can open different types of accounts (Savings, Current, FD).  
The system auto-generates a unique 12-digit account number and associates it with the user.  
The initial deposit is recorded at the time of account creation.

3. **Reporting & Dashboard**  
Customers can view their account details, balances, and transaction history.  
Admins have access to a comprehensive dashboard showing all user and account data.


## Authentication
Most endpoints require a JWT token obtained via `/login/`.  
Include the token in the `Authorization` header as:  


## Database Models
The application uses **Django ORM** with **SQLite**. Below are the database models, their fields, and relationships:

### User
Represents a user in the system.

| Field | Type | Description |
|-------|------|-------------|
| id | Integer | Primary key, unique identifier for the user |
| username | String | User’s username (required) |
| email | String | User’s email address (unique, required) |
| password | String | Hashed password using bcrypt (required) |
| role | String | Role of the user (`customer`, `admin`, `auditor`) |
| is_active | Boolean | Indicates if the user account is active |
| is_staff | Boolean | Required for admin permissions |
| is_superuser | Boolean | Indicates superuser status |

**Relationships:**  
- `accounts`: One-to-many relationship with Account (a user can have multiple accounts)

### Account
Represents a bank account owned by a user.

| Field | Type | Description |
|-------|------|-------------|
| id | Integer | Primary key, unique identifier for the account |
| account_number | String | Unique 12-digit account number, auto-generated |
| account_type | String | Type of account (Savings, Current, FD; required) |
| balance | Float | Current balance of the account (default: 0.0) |
| user_id | Integer | Foreign key referencing User.id |

**Relationships:**  
- `user`: Many-to-one relationship with User (each account belongs to one user)  
- `transactions`: One-to-many relationship with Transaction (optional, for future extension)

### Notes
- `account_number` is automatically generated as a unique 12-digit number during account creation.

### Transaction (Future Extension)
Represents a financial transaction (deposit, withdrawal, or transfer).

| Field | Type | Description |
|-------|------|-------------|
| id | Integer | Primary key, unique identifier for the transaction |
| account_id | Integer | Foreign key referencing Account.id |
| type | String | Transaction type (`withdraw`, `deposit`, `transfer`) |
| amount | Float | Transaction amount (required) |
| created_at | DateTime | Timestamp of creation (default: current UTC time) |

**Relationships:**  
- `account`: Many-to-one relationship with Account (each transaction is linked to one account)
