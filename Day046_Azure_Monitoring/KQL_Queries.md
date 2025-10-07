# 🔍 KQL – Kusto Query Language Examples

## 1️⃣ Failed Data Factory Pipelines

AzureDiagnostics
| where Category == "DataFactoryPipelineRun"
| summarize FailedRuns = countif(Status_s == "Failed") by PipelineName_s
| order by FailedRuns desc

## Databricks Job failures

AzureDiagnostics
| where ResourceProvider == "MICROSOFT.DATABRICKS"
| where Level == "Error"
| summarize count() by OperationName, bin(TimeGenerated, 1h)

## High CPU Usage alerts 

InsightsMetrics
| where Name == "Percentage CPU"
| summarize AvgCPU = avg(Val) by bin(TimeGenerated, 5m), Resource
| where AvgCPU > 80
