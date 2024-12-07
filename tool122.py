import numpy as np
from models import xgboost_anomaly_detection, isolation_forest_anomaly_detection, dbscan_anomaly_detection, train_lstm_model, arima_forecast
from network_analysis import consume_data_from_kafka, analyze_netflow_data
from cloud_integration import invoke_lambda
from alerts import setup_prometheus_alerts, trigger_alert_if_needed
from security import enable_mfa_for_key_management, manage_keys_with_hsm

class NetworkSecurityTool:
    def __init__(self, current_version, update_url):
        from update_notifier import UpdateNotifier
        self.update_notifier = UpdateNotifier(current_version, update_url)
        self.g = setup_prometheus_alerts()

    def check_for_updates(self):
        self.update_notifier.check_for_updates()

    def run_anomaly_detection(self, data):
        anomalies = self.analyze_data(data)
        self.trigger_alert(anomalies)

    def analyze_data(self, data):
        xgb_predictions = xgboost_anomaly_detection(data, data)
        isolation_forest_predictions = isolation_forest_anomaly_detection(data)
        dbscan_labels = dbscan_anomaly_detection(data)
        return xgb_predictions, isolation_forest_predictions, dbscan_labels

    def trigger_alert(self, anomalies):
        print("تحليل الشذوذ تم بنجاح.")
        if np.any(anomalies):
            print("تم اكتشاف شذوذ في البيانات.")

    def predict_network_performance(self, traffic_data):
        prediction = arima_forecast(traffic_data)
        return prediction

    def manage_keys(self):
        enable_mfa_for_key_management()
        manage_keys_with_hsm()

    def integrate_external_systems(self):
        invoke_lambda("aws_lambda_function", '{"data":"sample"}')

    def consume_network_data(self, topic):
        consume_data_from_kafka(topic)

    def analyze_netflow(self, file_path):
        analyze_netflow_data(file_path)
