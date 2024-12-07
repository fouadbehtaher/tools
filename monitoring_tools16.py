import requests

def zabbix_integration(host, metric, value):
    url = f'http://zabbix-server/api_jsonrpc.php'
    headers = {'Content-Type': 'application/json'}
    payload = {
        "jsonrpc": "2.0",
        "method": "item.create",
        "params": {
            "name": metric,
            "key_": metric,
            "hostid": host,
            "type": 0,
            "value_type": 3
        },
        "auth": "your_auth_token",
        "id": 1
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

def nagios_integration(host, metric, value):
    url = f'http://nagios-server/api'
    payload = {
        "host": host,
        "metric": metric,
        "value": value
    }
    response = requests.post(url, data=payload)
    return response.status_code
