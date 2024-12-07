from models import build_lstm_model, build_transformer_model, build_bert_model, train_model
from network_analysis import send_data_to_kafka, consume_data_from_kafka
from cloud_integration import upload_to_google_cloud, download_from_google_cloud
from alerts import setup_prometheus_alerts, trigger_alert_if_needed
from security import enable_mfa_for_key_management, manage_keys_with_hsm

class NetworkSecurityTool:
    def __init__(self):
        self.g = setup_prometheus_alerts()

    def run_anomaly_detection(self, data):
        model = build_transformer_model(data.shape[1:])
        model = train_model(model, data, data)
        anomalies = model.predict(data)
        self.trigger_alert(anomalies)

    def trigger_alert(self, anomalies):
        if anomalies.any():
            print("Anomaly detected!")

    def integrate_with_cloud(self, file_path, bucket_name):
        upload_to_google_cloud(file_path, bucket_name)
        download_from_google_cloud(file_path, bucket_name)

    def monitor_network(self, traffic_data):
        trigger_alert_if_needed(traffic_data)

    def manage_security(self):
        enable_mfa_for_key_management()
        manage_keys_with_hsm()
