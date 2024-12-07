from kafka import KafkaConsumer
import pyshark

def analyze_netflow_data(file_path):
    cap = pyshark.FileCapture(file_path)
    for packet in cap:
        print(packet)

def consume_data_from_kafka(topic):
    consumer = KafkaConsumer(topic, bootstrap_servers=['localhost:9092'])
    for message in consumer:
        print(message.value)
