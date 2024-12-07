from kafka import KafkaConsumer
import pyshark

# Analyze network data using NetFlow or sFlow
def analyze_netflow_data(file_path):
    cap = pyshark.FileCapture(file_path)
    for packet in cap:
        print(packet)

# Consume live data from Kafka
def consume_data_from_kafka(topic):
    consumer = KafkaConsumer(topic, bootstrap_servers=['localhost:9092'])
    for message in consumer:
        print(message.value)
