| Feature              | Normalization                        | Denormalization                       |
|----------------------|---------------------------------------|----------------------------------------|
| **Purpose**          | Reduce redundancy, improve integrity | Improve query performance              |
| **System Type**      | OLTP (transactional systems)          | OLAP (analytical systems)              |
| **Query Type**       | Frequent writes, simple reads         | Read-heavy, complex queries            |
| **Design**           | Multiple related tables               | Fewer tables with redundancy           |
| **Advantages**       | Saves space, avoids anomalies         | Faster queries, fewer joins            |
| **Disadvantages**    | More joins, slower reads              | Uses more storage, may cause anomalies |
| **Examples**         | Banking, E-commerce, ERP              | Data warehouses, BI dashboards         |
