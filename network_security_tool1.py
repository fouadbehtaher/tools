from anomaly_detection import ai_anomaly_detection
from time_series_analysis import train_lstm_model, arima_forecast
from encryption import multi_layer_encryption
from key_management import enable_mfa_for_key_management, manage_keys_with_hsm
from external_integrations import invoke_lambda, integrate_with_siem

class NetworkSecurityTool:
    def __init__(self):
        print("أداة أمن الشبكة قيد التشغيل.")
        
    def run_anomaly_detection(self, data):
        anomalies = ai_anomaly_detection(data)
        self.trigger_alert(anomalies)
        
    def trigger_alert(self, anomalies):
        print("تحليل الشذوذ تم بنجاح.")
        if anomalies.any():
            print("تم اكتشاف شذوذ في البيانات.")
    
    def encrypt_data(self, data):
        encrypted_data = multi_layer_encryption(data)
        return encrypted_data
    
    def manage_keys(self):
        enable_mfa_for_key_management()
        manage_keys_with_hsm()
        
    def integrate_external_systems(self):
        invoke_lambda("aws_lambda_function", '{"data":"sample"}')
        integrate_with_siem("sample_event_data")
    
    def predict_network_performance(self, traffic_data):
        prediction = arima_forecast(traffic_data)
        return prediction

    def analyze_network_time_series(self, network_data):
        lstm_model = train_lstm_model(network_data)
        return lstm_model
