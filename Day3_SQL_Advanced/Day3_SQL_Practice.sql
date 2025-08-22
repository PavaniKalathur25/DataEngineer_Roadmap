-- Day 3 SQL Practice

-- SUBQUERY (Find customers who spent above average amount)
SELECT customer_id, SUM(amount) as total_spent
FROM orders
GROUP BY customer_id
HAVING SUM(amount) > (
    SELECT AVG(amount) FROM orders
);

-- NESTED SUBQUERY (Find customers who placed the highest single order)
SELECT customer_id, order_id, amount
FROM orders
WHERE amount = (SELECT MAX(amount) FROM orders);

-- CTE (Common Table Expression) → cleaner subqueries
WITH customer_totals AS (
    SELECT customer_id, SUM(amount) AS total_spent
    FROM orders
    GROUP BY customer_id
)
SELECT c.customer_id, c.total_spent
FROM customer_totals c
WHERE c.total_spent > 500;

-- WINDOW FUNCTION → Ranking customers by total spending
SELECT customer_id, SUM(amount) AS total_spent,
       RANK() OVER (ORDER BY SUM(amount) DESC) AS spending_rank
FROM orders
GROUP BY customer_id;

-- ROW_NUMBER vs RANK example
SELECT order_id, customer_id, amount,
       ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY amount DESC) AS rownum,
       RANK() OVER (PARTITION BY customer_id ORDER BY amount DESC) AS ranknum
FROM orders;


