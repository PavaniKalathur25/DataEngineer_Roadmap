from azure.mgmt.consumption import ConsumptionManagementClient
from azure.identity import DefaultAzureCredential

credential = DefaultAzureCredential()
client = ConsumptionManagementClient(credential, "<subscription_id>")

for usage in client.usage_details.list(scope="/subscriptions/<subscription_id>"):
    print(usage.name, usage.pretax_cost)
