# Objectives

Download and install Kafka
Start the Zookeeper server for Kafka metadata management
Start the Kafka message broker service
Create a topic
Start a producer
Start a consumer

# Download and extract Kafka 
wget https://archive.apache.org/dist/kafka/2.8.0/kafka_2.12-2.8.0.tgz
tar -xzf kafka_2.12-2.8.0.tgz

# Start Zookeeper
cd kafka_2.12-2.8.0
bin/zookeeper-server-start.sh config/zookeeper.properties


ZooKeeper is responsible for the overall management of Kafka cluster.
It monitors the Kafka brokers and notifies Kafka if any broker or partition goes down, or if a new broker or partition goes up.

# Start the kafka broker service

cd kafka_2.12-2.8.0
bin/kafka-server-start.sh config/server.properties

# Create a topic

cd kafka_2.12-2.8.0
bin/kafka-topics.sh --create --topic news --bootstrap-server localhost:9092

# Start producer

You need a producer to send messages to Kafka. Run the command below to start a producer.

1
bin/kafka-console-producer.sh --topic news --bootstrap-server localhost:9092
Copied!
Once the producer starts, and you get the ‘>’ prompt, type any text message and press enter. Or you can copy the text below and paste. The below text sends three messages to kafka.

1
2
3
Good morning
Good day
Enjoy the Kafka lab

# Start Consumer

You need a consumer to read messages from kafka.

Open a new terminal.

Run the command below to listen to the messages in the topic news.

1
2
cd kafka_2.12-2.8.0
bin/kafka-console-consumer.sh --topic news --from-beginning --bootstrap-server localhost:9092
Copied!
You should see all the messages you sent from the producer appear here.

You can go back to the producer terminal and type some more messages, one message per line, and you will see them appear here.