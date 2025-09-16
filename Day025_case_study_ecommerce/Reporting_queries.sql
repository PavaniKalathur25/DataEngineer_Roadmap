-- Find total revenue per month
SELECT DATE_FORMAT(OrderDate, '%Y-%m') AS Month, SUM(Amount) AS TotalRevenue
FROM Orders
GROUP BY Month;

-- Find customer purchase history
SELECT c.Name, o.OrderID, o.OrderDate, o.Amount
FROM Orders o
JOIN Customers c ON o.CustomerID = c.CustomerID
ORDER BY c.Name, o.OrderDate;
