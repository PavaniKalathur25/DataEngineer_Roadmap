# Normalization (1NF, 2NF, 3NF)

## What is Normalization?
- Database design technique to organize data, reduce redundancy, and improve consistency.
- Implemented in **normal forms**.

**Keywords:** redundancy, anomalies, primary key, foreign key, consistency.

---

## 1NF (First Normal Form)
- Each cell should have **atomic values**.
- No repeating groups.
- Example ❌ `Hobbies = 'Cricket, Football'` → ✅ split into separate rows.

**Keywords:** Atomic values, primary key, repeating groups.

---

## 2NF (Second Normal Form)
- Must be in **1NF**.
- Remove **partial dependency** (non-key column should depend on the full composite key).
- Example: If `OrderID + ProductID` is the key, `CustomerName` should not depend only on `OrderID`.

**Keywords:** Partial dependency, composite key, foreign key.

---

## 3NF (Third Normal Form)
- Must be in **2NF**.
- Remove **transitive dependency** (non-key column should not depend on another non-key column).
- Example: `Employee → DepartmentID → DepartmentName` → Move `DepartmentName` to a new table.

**Keywords:** Transitive dependency, non-key attributes, integrity.
