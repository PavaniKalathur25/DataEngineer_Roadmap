
---

### 📄 `presentation_layer.md`
```markdown
# Presentation Layer (Gold)

**What is it?**  
The business-ready data layer. Data is aggregated, modeled, and structured for reporting or dashboards.

**Where it's actually used?**
- Consumed by Power BI, Synapse Analytics, and ML models.
- Used by business users, analysts, and executives.

**Why used?**
- Provides easy-to-use, query-optimized datasets.
- Speeds up BI dashboards and analytics queries.

**Any coding needed?**
Less transformation, more modeling (aggregations, joins).

**Sample SQL Query (Synapse)**
```sql
SELECT region, SUM(amount) AS total_sales
FROM curated.sales
GROUP BY region;
