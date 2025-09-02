-- ================================
-- DAY 9 SQL PRACTICE MARATHON
-- Covers Topics: Day1 - Day8
-- ================================

-- 🔹 DAY 1: Basics
1. SELECT * FROM Employees;
2. SELECT first_name, salary FROM Employees WHERE salary > 50000;
3. SELECT * FROM Employees ORDER BY join_date DESC;
4. SELECT DISTINCT department_id FROM Employees;
5. SELECT TOP 5 * FROM Employees ORDER BY salary DESC;

-- 🔹 DAY 2: Joins
6. SELECT e.first_name, d.department_name 
   FROM Employees e INNER JOIN Departments d ON e.department_id = d.department_id;
7. SELECT e.first_name, d.department_name 
   FROM Employees e LEFT JOIN Departments d ON e.department_id = d.department_id;
8. SELECT d.department_name, e.first_name 
   FROM Departments d RIGHT JOIN Employees e ON d.department_id = e.department_id;
9. SELECT e.first_name, d.department_name 
   FROM Employees e FULL JOIN Departments d ON e.department_id = d.department_id;
10. SELECT e.first_name, p.project_name 
    FROM Employees e CROSS JOIN Projects p;

-- 🔹 DAY 3: Aggregations & Window Functions
11. SELECT department_id, COUNT(*) AS emp_count 
    FROM Employees GROUP BY department_id;
12. SELECT department_id, AVG(salary) AS avg_sal 
    FROM Employees GROUP BY department_id HAVING AVG(salary) > 60000;
13. SELECT e.first_name, RANK() OVER (ORDER BY salary DESC) AS rnk 
    FROM Employees e;
14. SELECT e.first_name, DENSE_RANK() OVER (ORDER BY salary DESC) AS drnk 
    FROM Employees e;
15. SELECT e.first_name, LAG(salary,1) OVER (ORDER BY join_date) AS prev_sal 
    FROM Employees e;
16. SELECT e.first_name, LEAD(salary,1) OVER (ORDER BY join_date) AS next_sal 
    FROM Employees e;

-- 🔹 DAY 3: CTEs
17. WITH HighSalary AS (
       SELECT * FROM Employees WHERE salary > 70000
    )
    SELECT * FROM HighSalary;
18. WITH DeptCount AS (
       SELECT department_id, COUNT(*) AS cnt FROM Employees GROUP BY department_id
    )
    SELECT * FROM DeptCount WHERE cnt > 5;

-- 🔹 DAY 4: Advanced Joins
19. SELECT e1.first_name, e2.first_name AS Manager
    FROM Employees e1 INNER JOIN Employees e2 ON e1.manager_id = e2.emp_id; -- Self Join
20. SELECT e.first_name 
    FROM Employees e 
    WHERE NOT EXISTS (SELECT 1 FROM Projects p WHERE e.emp_id = p.emp_id); -- Anti Join
21. SELECT DISTINCT d.department_name 
    FROM Departments d
    WHERE EXISTS (SELECT 1 FROM Employees e WHERE e.department_id = d.department_id); -- Semi Join
22. SELECT e.first_name, p.project_name, c.client_name
    FROM Employees e 
    JOIN Projects p ON e.emp_id = p.emp_id 
    JOIN Clients c ON p.client_id = c.client_id; -- Nested Join

-- 🔹 DAY 5: Constraints
23. CREATE TABLE TestTable (
       id INT PRIMARY KEY,
       name VARCHAR(50) NOT NULL,
       age INT CHECK (age >= 18),
       email VARCHAR(100) UNIQUE
    );
24. INSERT INTO TestTable VALUES (1, 'John', 25, 'john@example.com');

-- 🔹 DAY 6: Subqueries
25. SELECT first_name, salary FROM Employees
    WHERE salary > (SELECT AVG(salary) FROM Employees);
26. SELECT first_name 
    FROM Employees
    WHERE department_id IN (SELECT department_id FROM Departments WHERE location = 'Hyderabad');

-- 🔹 DAY 7: Optimization
27. CREATE INDEX idx_salary ON Employees(salary);
28. SELECT * FROM Employees WHERE salary > 60000; -- uses index
29. EXPLAIN SELECT * FROM Employees WHERE department_id = 10;

-- 🔹 DAY 8: Case Studies
-- Sales dataset
30. SELECT customer_id, SUM(amount) AS total_spent 
    FROM Sales GROUP BY customer_id ORDER BY total_spent DESC;
31. SELECT product_id, COUNT(*) AS total_sold 
    FROM Sales GROUP BY product_id ORDER BY total_sold DESC;
32. SELECT region, SUM(amount) AS revenue 
    FROM Sales GROUP BY region;

-- E-commerce dataset
33. SELECT category, SUM(price*quantity) AS revenue
    FROM Orders GROUP BY category ORDER BY revenue DESC;
34. SELECT customer_id, COUNT(order_id) AS total_orders
    FROM Orders GROUP BY customer_id HAVING COUNT(order_id) > 5;
35. SELECT order_date, SUM(price*quantity) AS daily_sales
    FROM Orders GROUP BY order_date ORDER BY order_date;

-- 🔹 MIXED REVISION (36–50)
36. Find 2nd highest salary using subquery.
37. Find employee(s) who joined most recently.
38. List departments with no employees (Anti Join).
39. Show employees who earn above department average (Subquery).
40. Find top 3 earners per department (Window function + PARTITION BY).
41. Show employees hired before their managers (Self Join).
42. Show duplicate emails from Employees table.
43. List customers who never placed an order.
44. Find total employees per project (Join + Group By).
45. Rank customers by total spending (Rank window).
46. Show last 5 orders by each customer (Row_Number + Partition).
47. Get department with max employees (Aggregation).
48. Show revenue % contribution per category (Window + SUM).
49. Find projects with more than 3 employees assigned.
50. List employees earning within ±10% of department average salary.

