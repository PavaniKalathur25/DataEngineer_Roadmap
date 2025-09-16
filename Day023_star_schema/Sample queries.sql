-- Find total sales per customer
SELECT c.Name, SUM(o.Amount) AS TotalSpent
FROM Orders o
JOIN Customers c ON o.CustomerID = c.CustomerID
GROUP BY c.Name;

-- Find total sales per product category
SELECT p.Category, SUM(o.Amount) AS TotalSales
FROM Orders o
JOIN Products p ON o.ProductID = p.ProductID
GROUP BY p.Category;
