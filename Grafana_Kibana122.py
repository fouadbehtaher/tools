import requests

def push_data_to_grafana(data, dashboard_url):
    headers = {
        'Authorization': 'Bearer <Grafana API Token>',
    }
    response = requests.post(dashboard_url, json=data, headers=headers)
    return response.status_code

data = {
    "target": "network_traffic",
    "datapoints": [[123, 1636361812], [456, 1636361912]]
}
dashboard_url = "https://<grafana-server>/api/datasources/proxy/1/metrics"
response = push_data_to_grafana(data, dashboard_url)
print(response)
