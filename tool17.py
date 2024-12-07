from models import xgboost_anomaly_detection, train_lstm_model, arima_forecast, deep_learning_model
from network_analysis import consume_data_from_kafka, analyze_netflow_data
from cloud_integration import invoke_lambda
from alerts import setup_prometheus_alerts, trigger_alert_if_needed
from security import enable_mfa_for_key_management, manage_keys_with_hsm
from time_series_analysis import train_improved_lstm_model
from key_management import KeyManagement
from gui import NetworkSecurityToolGUI
from monitoring_tools import zabbix_integration, nagios_integration, grafana_integration

class NetworkSecurityTool:
    def __init__(self):
        self.g = setup_prometheus_alerts()
        self.key_manager = KeyManagement()

    def run_anomaly_detection(self, data, labels):
        anomalies = xgboost_anomaly_detection(data, labels)
        self.trigger_alert(anomalies)

    def trigger_alert(self, anomalies):
        print("Anomaly detection completed.")
        if np.any(anomalies):
            print("Anomalies detected!")

    def analyze_network_traffic(self, file_path):
        analyze_netflow_data(file_path)

    def integrate_with_external_systems(self):
        payload = '{"data":"sample"}'
        response = invoke_lambda('aws_lambda_function', payload)
        print(response)

    def predict_network_performance(self, data, labels):
        model = deep_learning_model(data, labels)
        print("Model trained successfully!")
        return model

    def manage_keys(self):
        enable_mfa_for_key_management()
        manage_keys_with_hsm()

    def integrate_with_monitoring_tools(self, host, metric, value):
        # Integrating with monitoring tools like Zabbix, Nagios, and Grafana
        zabbix_integration(host, metric, value)
        nagios_integration(host, metric, value)
        grafana_integration(data=value)  # Example: sending data to Grafana

    def run_gui(self):
        # Run the GUI
        import tkinter as tk
        root = tk.Tk()
        gui = NetworkSecurityToolGUI(root)
        root.mainloop()

tool = NetworkSecurityTool()

data = np.random.rand(100, 10)
labels = np.random.randint(2, size=100)
tool.run_anomaly_detection(data, labels)

network_data = np.random.rand(50, 5)
performance_model = tool.predict_network_performance(network_data, network_data)

tool.manage_keys()
tool.integrate_with_external_systems()

tool.run_gui()
