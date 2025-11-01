# Day 62 - Storage Systems: OLTP vs OLAP | Data Warehouses vs Data Lakes

## 📘 Overview
This day covers the backbone of data systems — how data is stored, processed, and analyzed.
You'll understand:
- The difference between OLTP and OLAP
- How Data Warehouses differ from Data Lakes
- Where each fits in a modern Azure-based data engineering architecture

---

## 🧩 Concepts Covered
| Concept | Description |
|----------|--------------|
| **OLTP** | Online Transaction Processing – handles real-time inserts, updates, deletes. |
| **OLAP** | Online Analytical Processing – designed for historical analysis and reporting. |
| **Data Warehouse** | Central store of structured data for analytics (e.g., Azure Synapse). |
| **Data Lake** | Raw storage for any data type (e.g., Azure Data Lake Storage). |

---

## ⚙️ Real-World Flow
1. **Data enters via OLTP systems** (SQL DB, apps, websites)
2. **Raw data lands in Data Lake** (ADLS)
3. **Data is cleaned and loaded into Data Warehouse** (Synapse / Snowflake)
4. **OLAP queries power dashboards** (Power BI / Tableau)

---

## 🧠 Keywords
- OLTP: Transactions, ACID, Normalization  
- OLAP: Aggregation, Star Schema, ETL/ELT  
- Data Warehouse: Schema-on-write, Structured Data  
- Data Lake: Schema-on-read, Semi-structured Data  

---

## 🔗 Azure Tools Used
| Stage | Azure Service |
|--------|----------------|
| OLTP | Azure SQL Database |
| Raw Data | Azure Data Lake Storage Gen2 |
| Processed Data | Azure Synapse Analytics |
| Visualization | Power BI |

---

## 🚀 Next Step
Move to **Day 63 → Modern Data Architecture** where you’ll connect these systems into one unified Azure data flow.
