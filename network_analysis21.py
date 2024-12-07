from kafka import KafkaProducer, KafkaConsumer
import json
import time

def send_data_to_kafka(topic, data):
    producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda x: json.dumps(x).encode('utf-8'))
    producer.send(topic, value=data)
    producer.flush()

def consume_data_from_kafka(topic):
    consumer = KafkaConsumer(topic, bootstrap_servers='localhost:9092', group_id='network_group', auto_offset_reset='earliest', value_deserializer=lambda x: json.loads(x.decode('utf-8')))
    for message in consumer:
        print(f"Received message: {message.value}")
        time.sleep(1)  
