# Day 3 Notes

# Day 3 – Intermediate SQL: Joins, CTEs, and Window Functions

## 1. Joins Recap
- **INNER JOIN** → Only matching rows.
- **LEFT JOIN** → All from left table + matches.
- **RIGHT JOIN** → All from right table + matches.
- **FULL OUTER JOIN** → All rows, match if possible.
- **SELF JOIN** → Join table with itself.

---

## 2. Common Table Expressions (CTE)

### What:
- A temporary result set used inside a query.
- Makes queries cleaner, reusable, and step-by-step.

### Why:
- Better readability compared to nested subqueries.
- Break down complex queries logically.

### Syntax:
```sql
WITH cte_name AS (
    SELECT ...
)
SELECT * FROM cte_name;

