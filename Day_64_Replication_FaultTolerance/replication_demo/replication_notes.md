# 🔁 Replication Notes

### What is Replication?
Replication is the process of copying data from one node (primary) to others (replicas) for durability and availability.

### Types of Replication
- **Synchronous:** Data written to all replicas before success is returned. (Strong consistency)
- **Asynchronous:** Primary writes first; replicas sync later. (Better performance)

### Example Systems
- **Kafka:** Topic replication factor = number of brokers storing same data.
- **Databases:** Read replicas used to offload read traffic from the primary node.

### Benefits
- Prevents data loss
- Enables high availability
- Improves read scalability
