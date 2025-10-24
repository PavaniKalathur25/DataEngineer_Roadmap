
---

## 💻 `Day3_SQL_Practice.sql`
```sql
-- Total sales
SELECT SUM(amount) FROM orders;

-- Avg order per customer
SELECT c.name, AVG(o.amount) AS avg_sales
FROM customers c
JOIN orders o ON c.cust_id = o.cust_id
GROUP BY c.name;

-- Rank customers
SELECT c.name, SUM(o.amount) AS total_sales,
       ROW_NUMBER() OVER (ORDER BY SUM(o.amount) DESC) AS row_num
FROM customers c
JOIN orders o ON c.cust_id = o.cust_id
GROUP BY c.name;

-- CTE for top 2 customers
WITH customer_sales AS (
  SELECT c.name, SUM(o.amount) AS total_sales
  FROM customers c
  JOIN orders o ON c.cust_id = o.cust_id
  GROUP BY c.name
)
SELECT * FROM customer_sales
ORDER BY total_sales DESC
LIMIT 2;
