# 📚 Library Management System

A console-based **Library Management System** developed with **Python** and **PostgreSQL**, following a layered architecture and software engineering best practices.

The project was created as a study case to apply concepts such as Object-Oriented Programming (OOP), database modeling, authentication, CRUD operations, and clean software architecture.

---

## 🚀 Technologies

* Python 3.x
* PostgreSQL
* Psycopg
* bcrypt
* python-dotenv

---

## 📂 Project Structure

```text
library-management-system/
│
├── app/
│   ├── controllers/
│   ├── database/
│   │   └── database.py
│   ├── models/
│   ├── repositories/
│   ├── services/
│   ├── utils/
│   └── main.py
│
├── database/
│   └── schema.sql
│
├── .env
├── requirements.txt
└── README.md
```

---

## 🏛️ Architecture

The application follows a layered architecture where each layer has a single responsibility.

```text
Controller
     │
     ▼
Service
     │
     ▼
Repository
     │
     ▼
Database
     │
     ▼
PostgreSQL
```

### Layers

* **Controllers**: Handle user interaction.
* **Services**: Contain business rules.
* **Repositories**: Execute SQL queries.
* **Models**: Represent database entities.
* **Database**: Manage PostgreSQL connections.
* **Utils**: Helper functions such as password hashing and validations.

---

## ✨ Features

### Authentication

* User registration
* Secure password hashing using bcrypt
* Login system
* Role-based access control

### User Roles

* Administrator
* Employee
* Customer

### Book Management *(Planned)*

* Register books
* Update books
* Delete books
* List books
* Search by title
* Search by author
* Search by ID

### Author Management *(Planned)*

* Register authors
* Update authors
* Delete authors
* List authors

### Category Management *(Planned)*

* Register categories
* Update categories
* Delete categories
* List categories

### Loan System *(Planned)*

* Rent books
* Return books
* Loan history
* Availability control

### Logs *(Planned)*

* User activity logging
* Audit history

---

## 🗄️ Database

The project uses PostgreSQL with a normalized relational model.

Current tables:

* `usuarios`
* `autores`
* `categorias`
* `livros`
* `emprestimos`
* `logs`

The database includes:

* Primary Keys
* Foreign Keys
* Named Constraints
* Check Constraints
* Indexes
* Default Values

---

## 🔒 Authentication

Passwords are never stored as plain text.

The application uses **bcrypt** to generate secure password hashes before persisting user credentials.

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/EduPanage/Library-Management-System-PY
```

Access the project directory:

```bash
cd library-management-system
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment.

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=Library
DB_USER=postgres
DB_PASSWORD=your_password
```

Create the database schema:

```bash
psql -d Library -f database/schema.sql
```

Run the application:

```bash
python app/main.py
```

---

## 📌 Current Status

### Completed

* Database modeling
* PostgreSQL integration
* Connection management
* Layered architecture
* User entity
* User repository
* Authentication service
* Password hashing
* User registration
* Login system

### In Progress

* Main menu
* Role-based navigation

### Planned

* Book management
* Author management
* Category management
* Loan system
* Return system
* Search filters
* Logging
* Reports

---

## 🎯 Learning Goals

This project was designed to practice:

* Object-Oriented Programming
* Software Architecture
* SOLID principles
* Repository Pattern
* Service Layer Pattern
* PostgreSQL
* Secure Authentication
* CRUD Operations
* Clean Code
* Python Best Practices

---

## 📄 License

This project is intended for educational purposes and portfolio development.
