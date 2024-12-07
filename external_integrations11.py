import boto3
from kafka import KafkaConsumer

def invoke_lambda(function_name, payload):
    lambda_client = boto3.client('lambda', region_name='us-east-1')
    response = lambda_client.invoke(
        FunctionName=function_name,
        InvocationType='RequestResponse',
        Payload=payload
    )
    return response['Payload'].read().decode('utf-8')

def integrate_with_siem(system_events):
    print("تحليل الأحداث الأمنية باستخدام نظم SIEM.")

def consume_data_from_kafka(topic):
    consumer = KafkaConsumer(topic, bootstrap_servers=['localhost:9092'])
    for message in consumer:
        print(message.value)
