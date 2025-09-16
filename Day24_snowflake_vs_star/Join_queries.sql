-- Join Orders with Product, Category, and Supplier
SELECT o.OrderID, p.ProductName, c.CategoryName, s.SupplierName, o.Quantity, o.Amount
FROM Orders o
JOIN Products p ON o.ProductID = p.ProductID
JOIN Categories c ON p.CategoryID = c.CategoryID
JOIN Suppliers s ON p.SupplierID = s.SupplierID;
