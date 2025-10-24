-- Query raw CSV data from Data Lake
SELECT TOP 10 *
FROM OPENROWSET(
    BULK 'https://yourstorageaccount.dfs.core.windows.net/container/sales/*.csv',
    FORMAT = 'CSV',
    PARSER_VERSION = '2.0',
    FIRSTROW = 2
) AS [result];
