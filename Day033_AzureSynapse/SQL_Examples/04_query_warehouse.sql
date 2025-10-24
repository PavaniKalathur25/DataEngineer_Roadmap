-- Join Fact & Dimension Tables
SELECT 
    f.SaleID,
    d.ProductName,
    f.Quantity,
    f.Amount,
    f.SaleDate
FROM FactSales f
JOIN DimProduct d ON f.ProductID = d.ProductID
ORDER BY f.SaleDate;
