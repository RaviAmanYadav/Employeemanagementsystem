# 📊 Employee Management System (Python + JSON)

## 🚀 Overview

This is a **Python-based Employee Management System** that allows you to manage employee records efficiently using **file handling (JSON)**.

The project is designed using a **modular and scalable architecture**, similar to real-world backend systems.

---

## 🧠 Features

### ✅ Implemented

* Add Employee
* Store employee data in JSON format
* Unique ID generation
* Clean modular structure

### ⚙️ In Progress / To Be Added

* View all employees
* Search employee by ID
* Update employee details
* Delete employee
* Input validation

---

## 🏗️ Project Structure

```
employee_management_system/
│
├── main.py
├── config/
│   └── settings.py
│
├── data/
│   └── employees.json
│
├── app/
│   ├── models/
│   │   └── employee.py
│   │
│   ├── repository/
│   │   └── employee_repo.py
│   │
│   ├── service/
│   │   └── employee_service.py
│   │
│   ├── utils/
│   │   └── helpers.py
│   │
│   └── presentation/
│       └── menu.py
│
└── README.md
```

---

## ⚙️ Tech Stack

* Python 3
* JSON (for data storage)
* File Handling
* CLI (Command Line Interface)

---

## 🔄 How It Works

```
User Input → Menu → Service Layer → Repository → JSON File
```

* **Presentation Layer** → Handles user input/output
* **Service Layer** → Business logic
* **Repository Layer** → File handling
* **Model** → Data structure

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/employee-management-system.git
```

2. Navigate to project folder:

```bash
cd employee-management-system
```

3. Run the project:

```bash
python main.py
```

---

## 📁 Data Storage

All employee data is stored in:

```
data/employees.json
```

Example:

```json
[
    {
        "emp_id": 1,
        "name": "Aman",
        "age": 25,
        "department": "Developer",
        "salary": 30000
    }
]
```

---

## 🧩 Key Concepts Used

* Object-Oriented Programming (OOP)
* Separation of Concerns
* File Handling (Read/Write JSON)
* Error Handling
* Clean Code Structure

---

## 🚧 Future Improvements

* Convert to Flask API
* Add database (PostgreSQL / MySQL)
* Add authentication (Admin/User)
* Add logging system
* Add unit testing

---

## 💡 Learning Outcome

This project helped in understanding:

* How real-world backend systems are structured
* How to separate logic, data, and presentation
* How to work with JSON as a database

---

## 📌 Author

**Aman**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub — it motivates to build more!
