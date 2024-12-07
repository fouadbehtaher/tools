from models import (
    train_autoencoder, train_lstm_model, xgboost_anomaly_detection, 
    isolation_forest_anomaly_detection, dbscan_anomaly_detection, 
    arima_forecast, prophet_analysis
)
from network_analysis import analyze_netflow_data, consume_data_from_kafka
from cloud_integration import invoke_lambda
from alerts import setup_prometheus_alerts, trigger_alert_if_needed
from security import enable_mfa_for_key_management, manage_keys_with_hsm

class NetworkSecurityTool:
    def __init__(self):
        self.g = setup_prometheus_alerts()

    def run_anomaly_detection(self, data):
        anomalies = ai_anomaly_detection(data)
        self.trigger_alert(anomalies)

    def trigger_alert(self, anomalies):
        print("تحليل الشذوذ تم بنجاح.")
        if np.any(anomalies):
            print("تم اكتشاف شذوذ في البيانات.")

    def visualize_results(self, results):
        pass

    def manage_keys(self):
        enable_mfa_for_key_management()
        manage_keys_with_hsm()

    def integrate_external_systems(self):
        invoke_lambda("aws_lambda_function", '{"data":"sample"}')

    def predict_network_performance(self, traffic_data):
        prediction = arima_forecast(traffic_data)
        return prediction

tool = NetworkSecurityTool()

data = np.random.rand(100, 10)  # بيانات عشوائية كمثال
tool.run_anomaly_detection(data)

network_data = np.random.rand(50, 5)
performance_prediction = tool.predict_network_performance(network_data)
print(performance_prediction)

tool.manage_keys()
tool.integrate_external_systems()
