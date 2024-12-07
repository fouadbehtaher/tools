import boto3

def invoke_lambda_for_data_processing(function_name, payload):
    lambda_client = boto3.client('lambda', region_name='us-east-1')
    response = lambda_client.invoke(
        FunctionName=function_name,
        InvocationType='RequestResponse',
        Payload=payload
    )
    result = response['Payload'].read().decode('utf-8')
    return result

payload = '{"network_data": [123, 456, 789]}'
function_name = "process_network_data"
result = invoke_lambda_for_data_processing(function_name, payload)
print(result)
