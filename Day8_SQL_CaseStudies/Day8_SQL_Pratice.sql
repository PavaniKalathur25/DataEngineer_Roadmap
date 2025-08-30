-- Create Sales Table
CREATE TABLE Sales (
    SaleID INT PRIMARY KEY,
    CustomerID INT,
    ProductID INT,
    Quantity INT,
    Price DECIMAL(10,2),
    SaleDate DATE
);

-- Insert sample sales data
INSERT INTO Sales VALUES
(1, 101, 1001, 2, 500.00, '2023-01-10'),
(2, 102, 1002, 1, 1200.00, '2023-01-12'),
(3, 103, 1001, 3, 500.00, '2023-02-01'),
(4, 101, 1003, 1, 700.00, '2023-02-15'),
(5, 104, 1002, 2, 1200.00, '2023-03-05');

-- Create Products Table
CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(50),
    Category VARCHAR(30)
);

INSERT INTO Products VALUES
(1001, 'Laptop', 'Electronics'),
(1002, 'Mobile', 'Electronics'),
(1003, 'Shoes', 'Fashion');

-- 1. Total sales per customer
SELECT CustomerID, SUM(Quantity*Price) AS TotalSpent
FROM Sales
GROUP BY CustomerID;

-- 2. Best-selling product
SELECT TOP 1 P.ProductName, SUM(S.Quantity) AS TotalSold
FROM Sales S
JOIN Products P ON S.ProductID = P.ProductID
GROUP BY P.ProductName
ORDER BY TotalSold DESC;

-- 3. Monthly sales trend
SELECT YEAR(SaleDate) AS Year, MONTH(SaleDate) AS Month, SUM(Quantity*Price) AS Revenue
FROM Sales
GROUP BY YEAR(SaleDate), MONTH(SaleDate)
ORDER BY Year, Month;

-- 4. Customers who bought Electronics only
SELECT DISTINCT CustomerID
FROM Sales S
JOIN Products P ON S.ProductID = P.ProductID
WHERE P.Category = 'Electronics';

-- 5. Top 2 customers by revenue
WITH CustomerRevenue AS (
    SELECT CustomerID, SUM(Quantity*Price) AS Revenue
    FROM Sales
    GROUP BY CustomerID
)
SELECT TOP 2 * FROM CustomerRevenue ORDER BY Revenue DESC;

