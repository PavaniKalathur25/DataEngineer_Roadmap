"""
Python Example - Sending messages to Azure Event Hub
"""

from azure.eventhub import EventHubProducerClient, EventData

connection_str = "<EVENT_HUB_CONNECTION_STRING>"
eventhub_name = "<EVENT_HUB_NAME>"

# Create Producer Client
producer = EventHubProducerClient.from_connection_string(
    conn_str=connection_str, eventhub_name=eventhub_name
)

# Create a batch of events
event_data_batch = producer.create_batch()
event_data_batch.add(EventData("Message from Data Engineer!"))
event_data_batch.add(EventData("Another streaming event"))

# Send the batch
producer.send_batch(event_data_batch)
print("Messages sent successfully!")
