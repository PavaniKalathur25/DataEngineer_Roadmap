
---

### 📂 **sql_examples/**

#### **01_create_dw_tables.sql**
```sql
-- Create Dimension Table
CREATE TABLE DimProduct (
    ProductID INT PRIMARY KEY,
    ProductName NVARCHAR(100),
    Category NVARCHAR(50)
);

-- Create Fact Table
CREATE TABLE FactSales (
    SaleID INT PRIMARY KEY,
    ProductID INT,
    Quantity INT,
    SaleDate DATE,
    Amount DECIMAL(10,2),
    FOREIGN KEY (ProductID) REFERENCES DimProduct(ProductID)
);
