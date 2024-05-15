# Create a topic 
kafka-topics --bootstrap-server localhost:9092 --topic log_topic --create --partitions 2 --replication-factor 2

# List topics
kafka-topics --bootstrap-server localhost:9092 --list

# Get topics details

kafka-topics --bootstrap-server localhost:9092 --describe log_topic

# Delete topics 

kafka-topics --bootstrap-server localhost:9092 --topic log_topic --delete

# Start a producer to a topic, without keys

kafka-console-producer --broker-list localhost:9092 --topic log_topic

# Start a producer to a topic with keys

kafka-console-producer --broker-list localhost:9092 --topic user_topic --property parse.key=true -property key-separator=,

# Kafka consumer

Consumers are clients subscribed to topics
Consume data in the same order

# Consumer CLI

- Read new events from the log_topic, offset 1:
kafka-console-consumer --bootstrap-server localhost:9092 --topic log_topic

- Read all events from the log_topic, offset =
kafka-console-consumer --bootstrap-server --topic log_topic --from-beginning

