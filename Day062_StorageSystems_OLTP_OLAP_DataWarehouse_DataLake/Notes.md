# Notes - OLTP vs OLAP, Data Warehouse vs Data Lake

## OLTP
- Fast, small transactions
- Keeps data consistent (ACID)
- Example: Inserting an order into E-commerce DB

```sql
INSERT INTO orders (order_id, user_id, amount, date)
VALUES (1001, 23, 499.99, GETDATE());
