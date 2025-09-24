# Streaming Processing - Intro to Real-time Data

This repo demonstrates the basics of real-time streaming:
- Continuous data ingestion & processing
- Difference from batch processing
- Example with Python (simulation)
- Example with PySpark + Kafka

## Structure
- `data/`: Sample events (JSON format).
- `python_simulation/event_stream.py`: Simple real-time event simulation.
- `pyspark_streaming/kafka_streaming.py`: PySpark Structured Streaming with Kafka.
- `requirements.txt`: Dependencies.

## How to Run
### Python Simulation
```bash
python python_simulation/event_stream.py

