
---

### 📄 `azure_compute.md`
```markdown
# Azure Compute Basics

**What is it?**  
Compute = Power of running things (machines, apps, jobs).

**Where it's actually used?**
- Running transformation jobs (PySpark in Databricks).
- Hosting applications/pipelines.
- Running ETL workloads or machine learning models.

**Why used (any coding needed)?**
- You need compute to process data, not just store it.
- Without compute, storage is just files sitting idle.
- Coding depends on the compute service:
  - Azure Functions → Python/C#/JavaScript code.
  - Databricks → PySpark/SQL code.
  - VMs → any programming language.

**Keywords:** VM, Databricks, Synapse, Functions, Kubernetes, Cluster, Autoscaling, Consumption Plan.
