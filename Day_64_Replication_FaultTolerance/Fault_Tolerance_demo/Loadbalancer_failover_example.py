import random

# Simulating load balancer failover mechanism
servers = ["Server_A", "Server_B", "Server_C"]

failed_server = random.choice(servers)
print(f"🚨 Failover Triggered: {failed_server} is DOWN!")

# Filter out failed server
active_servers = [s for s in servers if s != failed_server]
print(f"✅ Redirecting traffic to: {active_servers}")
