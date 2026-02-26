# ☕ Coffee Cart Management System  
**Object-Oriented Python Project | MVC Architecture | SQLite | AI Integration**

## 📌 Project Overview

Coffee Cart is a console-based management system developed in Python using Object-Oriented Programming principles and the MVC design pattern.

The system simulates a small coffee shop environment where users can:

- Create multi-item customer orders  
- Store orders in a local SQLite database  
- View full order history  
- Search orders by customer name  
- Analyze best-selling products  
- Generate AI-powered order insights using a local LLM (Ollama)

This project demonstrates modular architecture, separation of concerns, encapsulation, inheritance, polymorphism, operator overloading, and database integration.

---

## 🏗️ Architecture

The project follows the **MVC (Model–View–Controller)** pattern:

### Model
- `Product.py`
- `Coffee.py`
- `DatabaseManager.py`

Responsible for:
- Business logic
- Data modeling
- SQLite database interaction

### View
- `ConsoleView.py`

Responsible for:
- CLI interface
- User input and formatted output

### Controller
- `MainController.py`

Responsible for:
- Application flow
- REPL loop
- Coordinating between Model and View

### AI Module, Optional Bonus Feature
- `AIHandler.py`

Handles local LLM interaction using Ollama.

---

## 🧠 Object-Oriented Concepts Implemented

This project demonstrates:

- **Encapsulation**  
  Private attributes in `Product` class

- **Inheritance**  
  `Coffee` extends `Product`

- **Polymorphism**  
  `Coffee` overrides `get_price()` to adjust pricing dynamically

- **Operator Overloading**  
  `__repr__()` implementation for readable object representation

- **Modularity and Separation of Concerns**  
  Each logical unit is placed in a separate file

---

## 💾 Database

- SQLite local database `coffee_cart.db`
- Orders are stored as single entries per transaction
- Includes:
  - Order ID
  - Product details
  - Customer name
  - Total price
  - Timestamp

Additional data analysis:
- Best-selling product detection based on stored orders

---

## 🤖 AI Integration, Optional

The system connects to a local LLM server using Ollama.

When an order is completed:
- The system sends a prompt summarizing the order
- The model generates:
  - A short order summary
  - A humorous fortune cookie message

Model used:
`phi3:latest`

If AI connection fails, the system handles the exception gracefully.

---

## 🔁 REPL Loop

The system runs in a continuous CLI loop with the following options:

1. New Order  
2. View Full History  
3. Search by Customer Name  
4. Most Recommended, Best Seller  
5. Exit  

---

## 🚀 How to Run

1. Install Python 3.10 or higher
2. Install dependencies:
   ```
   pip install ollama
   ```
3. Make sure Ollama is running locally if using AI feature
4. Run:
   ```
   python MainController.py
   ```

---

## 🎯 Academic Objectives Achieved

✔ MVC architecture  
✔ SQLite integration  
✔ Modular code structure  
✔ REPL implementation  
✔ Object-oriented principles  
✔ AI integration bonus  


Developed as a final project in Object-Oriented Programming using Python.
