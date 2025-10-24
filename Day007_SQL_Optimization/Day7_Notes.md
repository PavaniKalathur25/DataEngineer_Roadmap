# Day 7: SQL Optimization Basics

## Execution Plans
- Show how SQL decides to run a query.
- Check in SSMS using **Ctrl + M**.

## Index Usage
- **Clustered Index** → Data stored physically (1 per table).
- **Non-Clustered Index** → Pointer to rows (many allowed).
- **Composite Index** → Useful when filtering on multiple columns.

## Common Pitfalls
- Avoid  (fetches unnecessary data).
- Avoid Non-SARGable queries (functions on columns).
  Example:  ❌
- Write SARGable queries for better performance.

