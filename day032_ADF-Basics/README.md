# Azure Data Factory (ADF) - Basics

This repo demonstrates the basics of ADF:
- Pipelines
- Linked Services
- Datasets

## Why ADF?
- Cloud-based ETL & orchestration tool
- Low-code drag & drop interface
- 100+ pre-built connectors (SQL, Blob, API, SaaS)
- Serverless & scalable

## Structure
- `pipeline/sample_pipeline.json` → Example ADF pipeline (Blob → SQL copy).
- `linked_services/` → Connections to data sources.
- `datasets/` → Definitions of input/output data structures.

## Core Concepts
- **Pipeline** → Workflow of activities (ETL process).
- **Linked Service** → Connection to source/destination.
- **Dataset** → Represents data (table, file, folder).
- **Integration Runtime (IR)** → Engine that runs pipeline.
- **Trigger** → Time-based or event-based scheduling.

## How to Use
1. Open ADF in Azure Portal.
2. Import JSON files into your ADF workspace.
3. Deploy & run pipeline.
4. Monitor execution in ADF Studio.
