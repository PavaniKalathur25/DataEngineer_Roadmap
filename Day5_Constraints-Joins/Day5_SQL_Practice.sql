-- Create Employees table with constraints
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    dept_id INT,
    salary DECIMAL(10,2)
);

-- Create Departments table with Foreign Key reference
CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50) NOT NULL
);

-- Add FK constraint (employees.dept_id references departments.dept_id)
ALTER TABLE employees
ADD CONSTRAINT fk_dept FOREIGN KEY (dept_id)
REFERENCES departments(dept_id);

-- Insert sample data
INSERT INTO departments VALUES
(1, 'HR'),
(2, 'IT'),
(3, 'Finance');

INSERT INTO employees VALUES
(101, 'Pavani', 'pavani@example.com', 2, 60000),
(102, 'Arjun', 'arjun@example.com', 1, 50000),
(103, 'Meera', NULL, 3, 70000);

-- Check constraints
-- 1. NOT NULL test → try inserting emp_name as NULL
INSERT INTO employees (emp_id, emp_name, email, dept_id, salary)
VALUES (104, NULL, 'test@example.com', 2, 40000); -- ❌ Fails

-- 2. UNIQUE test → duplicate email
INSERT INTO employees VALUES
(105, 'Kiran', 'pavani@example.com', 1, 45000); -- ❌ Fails

-- 3. FOREIGN KEY test → dept_id not in departments
INSERT INTO employees VALUES
(106, 'Sneha', 'sneha@example.com', 5, 55000); -- ❌ Fails

-- INDEX Example
CREATE INDEX idx_emp_name ON employees(emp_name);

-- Query using index
SELECT * FROM employees WHERE emp_name = 'Pavani';

