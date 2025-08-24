# Day 1 – SQL Foundations 🏗️

## 🌟 What is SQL?
- Structured Query Language → Language to communicate with databases.
- Think of it as **asking questions** to your data.

## 🧩 Where it's used?
- Banking → Transactions
- E-commerce → Products & orders
- Netflix → Watch history
- Hospitals → Patient records

## 🎯 Why it's used?
- Simple (English-like)
- Universal (works in MySQL, Postgres, SQL Server, Snowflake, BigQuery)
- Powerful (handles millions of rows)

---

## 🔑 Keywords
- **Database** → container of tables
- **Table** → rows (records) + columns (attributes)
- **DDL** (Data Definition Language) → CREATE, DROP
- **DML** (Data Manipulation Language) → SELECT, INSERT, UPDATE, DELETE
- **Query** → Question to the database

---

## 🛠️ Core Commands
```sql
-- Create table
CREATE TABLE students (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  grade INT
);

-- Insert rows
INSERT INTO students (id, name, grade)
VALUES (1, 'Pavani', 95),
       (2, 'Arjun', 88),
       (3, 'Meera', 76);

-- Fetch data
SELECT * FROM students;

-- Fetch with filter
SELECT * FROM students WHERE grade > 80;

-- Sorting
SELECT * FROM students ORDER BY grade DESC;

-- Limit results
SELECT * FROM students ORDER BY grade DESC LIMIT 2;
