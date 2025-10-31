#!/usr/bin/env bash
set -e
TOPIC=${1:-clickstream_topic}
PARTITIONS=${2:-3}
REPLICATION=${3:-1}

docker exec -it $(docker ps --filter "ancestor=confluentinc/cp-kafka:7.5.0" --format "{{.ID}}" | head -n1) \
  kafka-topics --bootstrap-server localhost:9092 --create --topic "$TOPIC" --partitions $PARTITIONS --replication-factor $REPLICATION || true

echo "Topic $TOPIC created (or already exists)."
