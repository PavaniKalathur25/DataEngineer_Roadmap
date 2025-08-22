# Day 3 Notes

# Day 3 Notes – Subqueries, CTEs & Window Functions

## SUBQUERY
- A query inside another query.
- Used when we need results from one query to filter another.
- Example: Customers spending above average.

## CTE (WITH Clause)
- Temporary named result set.
- Cleaner & reusable compared to nested subqueries.
- Example: Calculate totals first, then filter.

## WINDOW FUNCTIONS
- Perform calculations across a set of rows related to the current row.
- Do NOT collapse rows like GROUP BY.
- Examples: RANK, ROW_NUMBER, DENSE_RANK, SUM() OVER()

---

### 🎯 Real-Life Analogies
- **Subquery** → Asking your friend: "Tell me the top 5 movies, I’ll then check which one is available near me."  
- **CTE** → Writing a sticky note of calculations first, then using it multiple times.  
- **Window Functions** → School results: Each student’s score + their rank in class.

---

### 🔑 Interview Questions
1. Difference between **Subquery** & **CTE**? When would you use each?  
2. What’s the difference between **RANK(), DENSE_RANK(), and ROW_NUMBER()**?  
3. Can you filter a Window Function in WHERE? (Hint: No, must use CTE or subquery).  
4. Real-time case: Find the **top 2 orders per customer**.  
5. Why are Window Functions preferred over Subqueries sometimes?  

