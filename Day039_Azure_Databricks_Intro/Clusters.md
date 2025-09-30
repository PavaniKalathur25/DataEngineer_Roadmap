
---

### 📄 `clusters.md`
```markdown
# Databricks Clusters

**What is it?**  
A set of virtual machines (compute power) that run Spark jobs in Databricks.

**Where it's actually used?**
- Executes ETL jobs, ML training, and streaming pipelines.
- Shared by team members or dedicated for production workloads.

**Why used?**
- Spark jobs need distributed compute.
- Clusters can autoscale based on workload.

**Any coding needed?**
No coding for setup (done via UI/config).  
But PySpark/SQL code runs on clusters.

**Keywords:** Cluster, Autoscaling, Driver Node, Worker Node, Job Cluster, All-Purpose Cluster.
