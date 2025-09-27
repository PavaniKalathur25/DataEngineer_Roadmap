# Retry Policies in Pipelines

## What is it?
Defining rules to automatically re-run failed tasks.

## Where it's used?
- API ingestion pipelines.
- Cloud pipelines prone to transient failures.
- External database/file extractions.

## Why used?
- Ensures reliability.
- Prevents manual reruns.
- Makes pipelines fault tolerant.

## Coding Needed?
- Mostly configurations:
  - Airflow → `retries`, `retry_delay`.
  - ADF → Retry count & interval.

## Keywords
- Resilience, Fault Tolerance, Error Handling, Retry Count, Backoff Interval
