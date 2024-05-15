# Objectives

Use kafka-python to interact with Kafka server in Python
Send and receive messages through the Kafka-python client

# Create a topic in the Admin.py file

Install the kafka-python package by running the following command.
1
pip3 install kafka-python
Copied!
Create a new file named admin.py by running the following command.
1
touch admin.py
Copied!Executed!
Click the button below to open the file in edit mode and paste the following content in the file and save it.
 Open admin.py in IDE

from kafka.admin import KafkaAdminClient,NewTopic
admin_client = KafkaAdminClient(bootstrap_servers="localhost:9092", client_id='test')
topic_list = []
new_topic = NewTopic(name="bankbranch", num_partitions= 2, replication_factor=1)
topic_list.append(new_topic)
admin_client.create_topics(new_topics=topic_list)

#  Create a producer.py file

from kafka import KafkaProducer
import json
producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'))
producer.send("bankbranch", {'atmid':1, 'transid':100})
producer.send("bankbranch", {'atmid':2, 'transid':101})

producer.flush()

producer.close()

# Create Consumer.py file

from kafka import KafkaConsumer
consumer = KafkaConsumer('bankbranch',
                        group_id=None,
                         bootstrap_servers=['localhost:9092'],
                         auto_offset_reset = 'earliest')
print("Hello")
print(consumer)

for msg in consumer:
    print(msg.value.decode("utf-8"))