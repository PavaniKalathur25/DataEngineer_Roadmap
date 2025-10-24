
---

## 💻 `Day2_SQL_Practice.sql`
```sql
-- Customers & Orders Join Examples
SELECT c.name, o.order_id, o.amount
FROM customers c
INNER JOIN orders o ON c.cust_id = o.cust_id;

-- Customers without Orders
SELECT c.name
FROM customers c
LEFT JOIN orders o ON c.cust_id = o.cust_id
WHERE o.order_id IS NULL;

-- Orders without Customers
SELECT o.order_id
FROM orders o
LEFT JOIN customers c ON o.cust_id = c.cust_id
WHERE c.cust_id IS NULL;
