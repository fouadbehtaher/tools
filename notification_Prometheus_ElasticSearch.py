from prometheus_client import start_http_server, Gauge

def setup_prometheus_alerts():
    g = Gauge('network_traffic', 'Network Traffic Metric')
    start_http_server(8000)
    return g

from elasticsearch import Elasticsearch

def send_alert_to_elasticsearch(alert_message):
    es = Elasticsearch()
    es.index(index="alerts", document={"message": alert_message})
