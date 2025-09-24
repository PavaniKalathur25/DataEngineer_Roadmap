-- Insert sample data into DimProduct
INSERT INTO DimProduct VALUES (1, 'Laptop', 'Electronics');
INSERT INTO DimProduct VALUES (2, 'Phone', 'Electronics');

-- Insert sample data into FactSales
INSERT INTO FactSales VALUES (101, 1, 2, '2025-01-15', 2000.00);
INSERT INTO FactSales VALUES (102, 2, 1, '2025-01-20', 800.00);
