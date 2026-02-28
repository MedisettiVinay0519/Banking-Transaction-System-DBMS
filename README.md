🏦 Banking Transaction Management System
📌 Project Overview

This project is a DBMS-based Core Banking System designed and implemented from ER modeling to ACID-compliant transaction processing using MySQL and Python.

It simulates how real-world banking backend systems work by handling customer onboarding, account management, secure monetary transactions, audit logging, and reporting.

⚠️ This system represents an internal bank/admin backend, not a customer-facing application.


🧠 System Design Philosophy
🔹 Admin / Backend-Oriented System

The application is designed as an internal banking system operated by:

Bank staff

Administrators

Backend services

End-users (customers) typically interact with mobile/web apps, which internally call such systems.

This separation reflects real banking architecture.


🗂️ Entity Relationship (ER) Diagram

The system is designed based on a normalized ER model with strong referential integrity and role-based relationships.

📊 ER Diagram

![ER Diagram](er_diagram.png)

📁 Place the image file in the root of the repository:

🔹 ER Highlights

Customer → Account (1:M)

Account → Transaction (SENDS / RECEIVES)

Transaction → Transaction_Audit (Weak Entity)

Composite attributes (Name, Address)

Derived attribute (Age from DOB)

ACID-oriented transaction design
