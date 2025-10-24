-- Day 6 Practice: Views, Stored Procedures, Functions

-- 1. Create Sample Tables
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    name VARCHAR(50),
    salary DECIMAL(10,2),
    dept_id INT
);

CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50)
);

INSERT INTO employees VALUES
(1, 'Pavani', 60000, 1),
(2, 'Arjun', 55000, 2),
(3, 'Meera', 70000, 1),
(4, 'Ravi', 45000, 3);

INSERT INTO departments VALUES
(1, 'IT'), (2, 'HR'), (3, 'Finance');

-- 2. Create a View
CREATE VIEW emp_details AS
SELECT e.name, e.salary, d.dept_name
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id;

SELECT * FROM emp_details;

-- 3. Stored Procedure Example
CREATE PROCEDURE GetHighEarners @minSalary DECIMAL(10,2)
AS
BEGIN
    SELECT name, salary FROM employees WHERE salary > @minSalary;
END;

EXEC GetHighEarners 50000;

-- 4. Scalar Function Example
CREATE FUNCTION GetAnnualSalary(@monthly DECIMAL(10,2))
RETURNS DECIMAL(10,2)
AS
BEGIN
    RETURN @monthly * 12;
END;

SELECT name, dbo.GetAnnualSalary(salary/12) AS AnnualSalary
FROM employees;

-- 5. Table Function Example
CREATE FUNCTION GetEmployeesByDept(@dept INT)
RETURNS TABLE
AS
RETURN (SELECT name, salary FROM employees WHERE dept_id = @dept);

SELECT * FROM dbo.GetEmployeesByDept(1);

