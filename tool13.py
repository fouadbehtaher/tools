from models import xgboost_anomaly_detection, train_lstm_model
from network_analysis import consume_data_from_kafka, analyze_netflow_data
from cloud_integration import invoke_lambda
from alerts import setup_prometheus_alerts, trigger_alert_if_needed
from security import enable_mfa_for_key_management, manage_keys_with_hsm
from time_series_analysis import train_improved_lstm_model
from key_management import KeyManagement

class NetworkSecurityTool:
    def __init__(self):
        self.g = setup_prometheus_alerts()
        self.key_manager = KeyManagement()

    def run_anomaly_detection(self, data, labels):
        anomalies = xgboost_anomaly_detection(data, labels)
        self.trigger_alert(anomalies)

    def trigger_alert(self, anomalies):
        print("تحليل الشذوذ تم بنجاح.")
        if np.any(anomalies):
            print("تم اكتشاف شذوذ في البيانات.")

    def analyze_network_traffic(self, file_path):
        analyze_netflow_data(file_path)

    def integrate_with_external_systems(self):
        payload = '{"data":"sample"}'
        response = invoke_lambda('aws_lambda_function', payload)
        print(response)

    def predict_network_performance(self, data, labels):
        model = train_improved_lstm_model(data, labels)
        print("تم تدريب نموذج LSTM")
        return model

    def manage_keys(self):
        enable_mfa_for_key_management()
        manage_keys_with_hsm()

tool = NetworkSecurityTool()

data = np.random.rand(100, 10)  
labels = np.random.randint(2, size=100)  
tool.run_anomaly_detection(data, labels)

network_data = np.random.rand(50, 5)
performance_model = tool.predict_network_performance(network_data, network_data)

tool.manage_keys()
tool.integrate_with_external_systems()

tool.analyze_network_traffic("netflow_data.pcap")
