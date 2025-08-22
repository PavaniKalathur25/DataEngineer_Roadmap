# Day 1 Notes – SQL Foundations

## SELECT
- Pulls data from tables.
- Example: `SELECT name, age FROM employees;`

## WHERE
- Filters rows before grouping.
- Example: `WHERE amount > 1000`

## ORDER BY
- Sorts data ascending/descending.
- Example: `ORDER BY join_date DESC`

## GROUP BY
- Groups rows by column(s) for aggregation.
- Example: `GROUP BY customer_id`

## HAVING
- Filters groups after aggregation.
- Example: `HAVING SUM(amount) > 5000`

## LIMIT
- Restricts number of rows.
- Example: `LIMIT 5`

### 🎯 Real-Life Analogy
- **WHERE** = check people at entrance of cinema hall.  
- **GROUP BY** = divide them into groups (age, ticket type).  
- **HAVING** = apply conditions on those groups (e.g., groups with >10 people).  
- **ORDER BY** = arrange groups (smallest → biggest).  
- **LIMIT** = show only top groups. "
