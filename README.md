# 🏦 Banking Transaction Management System

---

## 📌 Project Overview
This project is a **DBMS-based Core Banking System** designed and implemented from **ER modeling to ACID-compliant transaction processing** using **MySQL and Python**.

It simulates how **real-world banking backend systems** operate by handling:
- Customer onboarding  
- Account lifecycle management  
- Secure monetary transactions  
- Audit logging  
- Reporting and statements  

⚠️ **Note:**  
This system represents an **internal bank/admin backend**, not a customer-facing application.

---

## 🧠 System Design Philosophy

### 🔹 Admin / Backend-Oriented System
The application is designed as an **internal banking system** operated by:
- Bank staff  
- Administrators  
- Backend services  

End-users (customers) typically interact with **mobile/web applications**, which internally communicate with such backend systems.

This separation closely reflects **real-world banking architecture**.

---

## 🗂️ Entity Relationship (ER) Diagram

The system is designed using a **normalized ER model** with strong referential integrity and role-based relationships.

### 📊 ER Diagram
![ER Diagram](Banking_Schema.png)

📁 Place the ER diagram image in the **root of the repository**.

### 🔹 ER Highlights
- Customer → Account (**1 : M**)  
- Account → Transaction (**SENDS / RECEIVES**)  
- Transaction → Transaction_Audit (**Weak Entity**)  
- Composite attributes (Name, Address)  
- Derived attribute (Age from DOB)  
- ACID-oriented transaction design  

---

## 🧱 Database Schema

### Tables
- `customers`
- `accounts`
- `transactions`
- `transaction_audit`

### Key DBMS Features
- Primary & Foreign Keys  
- CHECK constraints (e.g., balance ≥ 0)  
- Role-based transaction modeling  
- Soft deletes using account status  
- Weak entity implementation  

---

## 🔄 Core Functionalities

### 👨‍💼 Admin / Bank Operations
- Create Customer  
- Create Account  
- Block / Unblock Account  
- Close Account (Soft Close)  

### 💳 Account Operations
- Deposit Money  
- Withdraw Money  
- Transfer Funds  
- Check Balance  

### 📊 Reporting
- Transaction History  
- Monthly Statement (Opening Balance, Credits, Debits, Closing Balance)  

---

## 🔐 Account Status Enforcement

| Account Status | Allowed Operations |
|---------------|--------------------|
| ACTIVE | Deposit, Withdraw, Transfer |
| BLOCKED | Balance Check, Transaction History |
| CLOSED | Balance Check, Transaction History |

Monetary operations are **restricted** for BLOCKED and CLOSED accounts, while data visibility is preserved.

---

## ⚙️ ACID Transaction Handling

All monetary operations are:
- Wrapped in database transactions  
- Controlled via `COMMIT` and `ROLLBACK`  
- Protected using row-level locking  
- Audited for both success and failure  

This ensures:
- **Atomicity**
- **Consistency**
- **Isolation**
- **Durability**

---

## 🧩 Project Structure

```text
banking-system/
│
├── main.py
├── db_connection.py
├── create_customer.py
├── create_account.py
├── banking_operations.py
├── transaction_history.py
├── monthly_statement.py
├── account_service.py
├── admin_service.py
├── schema.sql
└── Banking_Schema.png
```
🎯 Key Learnings & Concepts

-ER to relational schema conversion
-Database normalization (3NF)
-Weak entities and identifying relationships
-ACID-compliant transaction processing
-Backend system design
-Real-world banking constraints

