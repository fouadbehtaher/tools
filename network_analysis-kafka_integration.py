from kafka import KafkaConsumer

def consume_data_from_kafka(topic):
    consumer = KafkaConsumer(topic, bootstrap_servers=['localhost:9092'])
    for message in consumer:
        print(f"Received message: {message.value}")
