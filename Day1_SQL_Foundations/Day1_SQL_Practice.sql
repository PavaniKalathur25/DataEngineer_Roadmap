-- Select specific columns
SELECT name, age FROM employees;

-- Filter with WHERE
SELECT * FROM orders WHERE amount > 1000;

-- Sorting
SELECT * FROM customers ORDER BY join_date DESC;

-- Aggregation
SELECT customer_id, SUM(amount) AS total_spend
FROM orders
GROUP BY customer_id;

-- Aggregation with HAVING
SELECT customer_id, SUM(amount) AS total_spend
FROM orders
GROUP BY customer_id
HAVING SUM(amount) > 5000;

-- Find top 5 products by sales
SELECT product_id, SUM(amount) AS total_sales
FROM orders
GROUP BY product_id
ORDER BY total_sales DESC
LIMIT 5;

