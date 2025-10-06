# 🔐 RBAC & IAM Overview

## What is it?
Azure RBAC and IAM help control who can access resources and what actions they can perform.
They ensure the right people (or services) have the right level of access.

## Where It’s Used
- Giving Data Engineers read/write access to Azure Data Lake.
- Allowing Databricks jobs to access ADLS securely.
- Restricting Power BI users to certain datasets.

## Why Used
- To prevent unauthorized data access.
- To simplify permission management.
- To enable secure automation via service identities.

## Key Concepts
| Keyword | Description |
|----------|--------------|
| **RBAC (Role-Based Access Control)** | Assigns access based on predefined roles |
| **IAM (Identity & Access Management)** | Manages users, groups, and permissions |
| **Tenant ID** | Azure AD directory identifier |
| **Role Assignments** | Bind roles to users or service principals |
| **Scope** | The level at which a role applies (subscription, resource group, resource) |
