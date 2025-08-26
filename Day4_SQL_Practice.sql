-- ================================================
-- Day 4 SQL Practice - Advanced Joins
-- Self Join, Nested Join, Semi Join, Anti Join
-- ================================================

-- Drop old tables if already exist
DROP TABLE IF EXISTS Employees;
DROP TABLE IF EXISTS Departments;
DROP TABLE IF EXISTS Projects;

-- ================================================
-- Step 1: Create Tables
-- ================================================

CREATE TABLE Departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50)
);

CREATE TABLE Projects (
    project_id INT PRIMARY KEY,
    project_name VARCHAR(50)
);

CREATE TABLE Employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(50),
    manager_id INT NULL,
    department_id INT,
    project_id INT NULL,
    FOREIGN KEY (department_id) REFERENCES Departments(department_id),
    FOREIGN KEY (project_id) REFERENCES Projects(project_id),
    FOREIGN KEY (manager_id) REFERENCES Employees(employee_id)
);

-- ================================================
-- Step 2: Insert Sample Data
-- ================================================

INSERT INTO Departments VALUES
(1, 'IT'),
(2, 'HR'),
(3, 'Finance');

INSERT INTO Projects VALUES
(101, 'Migration Project'),
(102, 'Recruitment Drive'),
(103, 'Budget Planning');

INSERT INTO Employees VALUES
(1, 'Alice', NULL, 1, 101),   -- Alice is IT head
(2, 'Bob', 1, 1, 101),        -- Bob reports to Alice
(3, 'Charlie', 1, 1, NULL),   -- Charlie reports to Alice but no project
(4, 'David', 2, 2, 102),      -- HR employee
(5, 'Eva', 2, 2, NULL),       -- HR employee no project
(6, 'Frank', 4, 2, 102),      -- HR employee under David
(7, 'Grace', 1, 3, 103);      -- Finance employee under Alice

-- ================================================
-- Step 3: Queries to Practice
-- ================================================

-- 1. SELF JOIN (Employee - Manager relationship)
SELECT 
    e.employee_id AS EmployeeID,
    e.name AS EmployeeName,
    m.name AS ManagerName
FROM Employees e
JOIN Employees m
    ON e.manager_id = m.employee_id;

-- 2. NESTED JOIN (Employee + Department + Project)
SELECT 
    e.name AS EmployeeName,
    d.department_name,
    p.project_name
FROM Employees e
JOIN Departments d
    ON e.department_id = d.department_id
JOIN Projects p
    ON e.project_id = p.project_id;

-- 3. SEMI JOIN (Employees who are assigned to a project)
SELECT e.name
FROM Employees e
WHERE EXISTS (
    SELECT 1
    FROM Projects p
    WHERE e.project_id = p.project_id
);

-- 4. ANTI JOIN (Employees who are NOT assigned to any project)
SELECT e.name
FROM Employees e
WHERE NOT EXISTS (
    SELECT 1
    FROM Projects p
    WHERE e.project_id = p.project_id
);
