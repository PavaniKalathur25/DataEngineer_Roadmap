# Day 3 – SQL Aggregations & CTEs 📊

## 🌟 What are Aggregations?
- Functions that summarize multiple rows into one value.

## 🔑 Common Aggregates
- COUNT() → number of rows
- SUM() → total value
- AVG() → average
- MIN(), MAX() → min/max value

---

## 🛠️ Grouping & Filtering
```sql
-- Sales per customer
SELECT c.name, SUM(o.amount) AS total_sales
FROM customers c
JOIN orders o ON c.cust_id = o.cust_id
GROUP BY c.name;

-- Filter with HAVING
SELECT c.name, SUM(o.amount) AS total_sales
FROM customers c
JOIN orders o ON c.cust_id = o.cust_id
GROUP BY c.name
HAVING SUM(o.amount) > 600;
