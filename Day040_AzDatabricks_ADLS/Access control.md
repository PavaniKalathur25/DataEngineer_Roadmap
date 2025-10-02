---

### 📄 `access_control.md`
```markdown
# Access Control in Databricks + ADLS

**What is it?**  
- Rules that decide who can access which data and what actions they can perform.
- Achieved via Azure RBAC (Role-Based Access Control) + ADLS ACLs (Access Control Lists).

**Where it's actually used?**
- Ensures only authorized users/jobs access sensitive data.
- Different teams (Data Engineers, Analysts, Scientists) get different permissions.

**Why used?**
- Security → protects sensitive data (PII, financial).
- Governance → ensures compliance (GDPR, HIPAA).

**Any coding needed?**
- Mostly configuration in Azure Portal (IAM roles, ACLs).
- Sometimes managed programmatically (PySpark/Hadoop API).

**Sample Code**
```bash
# Set ACLs via Azure CLI
az storage fs access set \
  --account-name storageaccount \
  --file-system raw \
  --path sales/ \
  --acl "user:<object-id>:rwx"
