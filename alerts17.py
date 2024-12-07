from prometheus_client import Gauge, start_http_server

def setup_prometheus_alerts():
    g = Gauge('network_traffic', 'Network Traffic Metric')
    start_http_server(8000)
    return g

def trigger_alert_if_needed(g, value):
    if value > 1000:  
        g.set(1)
    else:
        g.set(0)
