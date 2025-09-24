## Start Kafka & create topic:
kafka-topics.sh --create --topic realtime_events --bootstrap-server localhost:9092

## Produce messages into Kafka:
kafka-console-producer.sh --topic realtime_events --bootstrap-server localhost:9092

## Run PySpark job:
spark-submit pyspark_streaming/kafka_streaming.py
