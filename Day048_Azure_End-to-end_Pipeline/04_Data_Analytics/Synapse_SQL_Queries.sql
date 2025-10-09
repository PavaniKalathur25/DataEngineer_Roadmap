-- Create external table for processed data
CREATE EXTERNAL TABLE sales_summary (
  region NVARCHAR(50),
  total_sales FLOAT
)
WITH (
  LOCATION = '/processed/sales_by_region/',
  DATA_SOURCE = ecommerce_datalake,
  FILE_FORMAT = parquet_file
);

-- Sample query for Power BI
SELECT region, SUM(total_sales) AS total
FROM sales_summary
GROUP BY region;
