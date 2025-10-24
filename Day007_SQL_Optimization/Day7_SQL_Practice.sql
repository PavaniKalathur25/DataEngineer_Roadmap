-- Check Execution Plan in SSMS
-- Shortcut: Ctrl + M before executing query

-- Bad practice (SELECT * brings all columns)
SELECT * FROM Employees;

-- Better practice (fetch only required columns)
SELECT EmpID, EmpName, Department FROM Employees;

-- Index usage example
CREATE INDEX idx_dept ON Employees(Department);

SELECT EmpName FROM Employees WHERE Department = 'IT';

-- Non-SARGable query (index not used)
SELECT EmpName FROM Employees WHERE YEAR(JoiningDate) = 2023;

-- SARGable query (index can be used)
SELECT EmpName FROM Employees 
WHERE JoiningDate >= '2023-01-01' AND JoiningDate < '2024-01-01';

-- Composite index usage
CREATE INDEX idx_dept_salary ON Employees(Department, Salary);

SELECT EmpName 
FROM Employees 
WHERE Department = 'Finance' AND Salary > 50000;

