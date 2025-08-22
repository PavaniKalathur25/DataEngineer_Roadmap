# Day 2 Notes

# Day 2 Notes – SQL Joins

## INNER JOIN
- Returns rows with matching keys in both tables.
- Example: Customers who placed an order.

## LEFT JOIN
- All rows from LEFT table + matches from RIGHT.
- Example: All customers, even if no orders yet.

## RIGHT JOIN
- All rows from RIGHT table + matches from LEFT.
- Example: All orders, even if customer info is missing.

## FULL OUTER JOIN
- Combines LEFT + RIGHT join.
- Example: All customers and all orders, matched where possible.

## SELF JOIN
- Table joins with itself.
- Example: Employee → Manager relationships.

---

### 🎯 Real-Life Analogy
- **INNER JOIN** → Only couples who came together are allowed in photo.  
- **LEFT JOIN** → All people from bride’s side must appear in photo (groom side if matched).  
- **RIGHT JOIN** → All people from groom’s side must appear (bride side if matched).  
- **FULL OUTER JOIN** → Everyone from both families in photo, even if standing alone.  
- **SELF JOIN** → Family tree photo (child pointing to parent).  

---

### 🔑 Interview Questions
1. Difference between **WHERE vs ON** in JOINs?  
2. When would you use **LEFT JOIN** instead of INNER JOIN?  
3. Give a real-time case for **SELF JOIN**.  
4. Which join is most expensive in performance? Why?  
5. How do you find customers with **no orders**?  
   (Hint: LEFT JOIN + WHERE order_id IS NULL)

