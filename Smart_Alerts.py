from prometheus_client import Gauge, start_http_server

def setup_prometheus_alerts():
    g = Gauge('network_traffic', 'Network Traffic Metric')
    start_http_server(8000)
    return g

def setup_elasticsearch_alerts():
    from elasticsearch import Elasticsearch
    es = Elasticsearch()
    res = es.search(index="network-logs", body={"query": {"match": {"event": "anomaly"}}})
    return res
