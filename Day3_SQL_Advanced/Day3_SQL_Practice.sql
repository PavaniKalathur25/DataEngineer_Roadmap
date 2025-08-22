-- Day 3 SQL Practice


---

## 💻 `Day3_SQL_Practice.sql`
```sql
-- 1. INNER JOIN Practice
SELECT o.order_id, c.customer_name, o.amount
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id;

-- 2. LEFT JOIN Practice
SELECT c.customer_name, o.order_id, o.amount
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id;

-- 3. CTE Example
WITH customer_totals AS (
    SELECT customer_id, SUM(amount) AS total_spent
    FROM orders
    GROUP BY customer_id
)
SELECT customer_id, total_spent
FROM customer_totals
WHERE total_spent > 5000;

-- 4. Window Function – Ranking
SELECT student_id, score,
       RANK() OVER (ORDER BY score DESC) AS rank
FROM students;

-- 5. Window Function – Running Total
SELECT city, order_id, amount,
       SUM(amount) OVER (PARTITION BY city ORDER BY order_id) AS running_total
FROM orders;
