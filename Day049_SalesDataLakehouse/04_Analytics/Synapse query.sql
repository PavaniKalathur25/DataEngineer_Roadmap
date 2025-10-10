-- Query Delta/Parquet files from Synapse Serverless SQL
SELECT region, SUM(total_sales) AS total_sales
FROM OPENROWSET(
  BULK 'https://<account>.dfs.core.windows.net/gold/sales_summary_delta/',
  FORMAT='PARQUET'
) AS data
GROUP BY region;
