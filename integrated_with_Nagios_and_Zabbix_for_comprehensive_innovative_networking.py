import requests

def send_to_splunk(data):
    splunk_url = 'http://localhost:8088'
    headers = {'Authorization': 'Splunk YOUR_SPLUNK_TOKEN'}
    response = requests.post(splunk_url, headers=headers, data=data)
    return response
