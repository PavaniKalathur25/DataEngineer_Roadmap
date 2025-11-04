# 🧭 Architecture Diagrams

### Lambda Architecture Diagram
[Batch Layer] ---> [Serving Layer] <--- [Speed Layer]
(Data Lake)        (Unified Output)     (Stream Processor)

### Kappa Architecture Diagram
[Event Stream] ---> [Stream Processor] ---> [Storage/Serving Layer]
(Kafka)              (Spark/Flink)           (Delta Lake / Power BI)
