
---

## 💻 `Day1_SQL_Practice.sql` (Practice File)

```sql
-- Create Books table
CREATE TABLE books (
  id INT PRIMARY KEY,
  title VARCHAR(100),
  author VARCHAR(50),
  price DECIMAL(10,2)
);

-- Insert records
INSERT INTO books VALUES
(1, 'Data Magic 101', 'Rowling', 250),
(2, 'Python Sparks', 'Sam', 199),
(3, 'SQL Mastery', 'John', 300);

-- Show all books
SELECT * FROM books;

-- Books above 200
SELECT * FROM books WHERE price > 200;

-- Books by Rowling
SELECT * FROM books WHERE author = 'Rowling';
