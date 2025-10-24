# Day 5 – SQL Constraints & Keys

## 🔑 What are Constraints?
Rules applied on columns to maintain **data integrity** & **accuracy**.

### 1. PRIMARY KEY
- Uniquely identifies each row.
- Combines **NOT NULL** + **UNIQUE**.
- Only one primary key per table (can be composite across multiple columns).

### 2. FOREIGN KEY
- Establishes relationship between two tables.
- References the primary key in another table.
- Ensures **referential integrity**.

### 3. UNIQUE
- Ensures all values in a column are unique.
- Unlike PK, allows **NULL** (only once in most databases).

### 4. NOT NULL
- Column must always have a value.
- Used when the field is mandatory.

### 5. INDEX
- Improves query performance on large data.
- Creates a quick lookup path (like an index in a book).
- Downsides: Takes storage & slows down .

---

## 🌍 Real-World Usage
- **Primary Key** → Employee ID in HR systems.
- **Foreign Key** → Order linked to Customer.
- **Unique** → Email in a registration system.
- **Not Null** → Password field must not be empty.
- **Index** → Searching products by name in e-commerce.

---

## 🎯 Interview Quick Wins
**Q: Difference between Primary Key and Unique?**  
👉 PK = Unique + Not Null, only one allowed. Unique = multiple allowed, allows NULLs.  

**Q: Why do we need Foreign Key?**  
👉 To maintain relationships (Orders can’t exist without Customers).  

**Q: When to use Indexes?**  
👉 When queries are slow on large tables with frequent lookups.

---

