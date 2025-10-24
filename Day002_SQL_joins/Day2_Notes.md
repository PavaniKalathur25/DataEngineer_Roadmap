# Day 2 – SQL Joins & Filters 🔗

## 🌟 What are Joins?
- Combine rows from 2+ tables based on a related column.

## 🔑 Types of Joins
- INNER JOIN → Only matching rows
- LEFT JOIN → All left + matched right
- RIGHT JOIN → All right + matched left
- FULL JOIN → All rows (match + non-match)
- CROSS JOIN → Cartesian product

## 🧩 Filters
- WHERE → basic condition
- AND / OR → combine conditions
- IN → multiple values
- LIKE → pattern match
- IS NULL → check missing values

---

## 🛠️ Key Queries
```sql
-- INNER JOIN
SELECT c.name, o.order_id, o.amount
FROM customers c
INNER JOIN orders o ON c.cust_id = o.cust_id;

-- LEFT JOIN
SELECT c.name, o.order_id, o.amount
FROM customers c
LEFT JOIN orders o ON c.cust_id = o.cust_id;

-- Filter: Orders > 400
SELECT * FROM orders WHERE amount > 400;
