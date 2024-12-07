from models import build_autoencoder, xgboost_anomaly_detection, prophet_analysis, arima_forecast
from network_analysis import network_analysis
from cloud_integration import invoke_lambda, upload_to_google_cloud
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
        upload_to_google_cloud("your_bucket", "file_name", "file_path")

    def predict_network_performance(self, traffic_data):
        prediction = arima_forecast(traffic_data)
        return prediction
