from key_management import encrypt_data_with_aes, encrypt_data_with_rsa, generate_otp
from anomaly_detection import detect_anomaly_with_dbscan, detect_anomaly_with_autoencoder
from network_analysis import analyze_network_time_series, analyze_netflow_data
from security_tools import run_snort_for_ids, detect_ddos_attack
from performance_prediction import predict_network_performance, analyze_congestion
from alerting_tools import setup_prometheus_alerts, send_alert_to_elasticsearch
from integration_tools import send_to_splunk
from visualization_tools import plot_network_data


otp = generate_otp("JBSWY3DPEHPK3PXP")
print(f"Generated OTP: {otp}")

key = b'Sixteen byte key'
encrypted_data_aes = encrypt_data_with_aes("Sensitive Data", key)
print(f"Encrypted Data (AES): {encrypted_data_aes}")

network_data = np.random.random((100, 4))
predictions = detect_anomaly_with_dbscan(network_data)
print(f"Anomaly Detection Results: {predictions}")

data = {'ds': pd.date_range(start='2023-01-01', periods=10, freq='D'), 'y': np.random.random(10)}
forecast = predict_network_performance(data)
print(f"Network Performance Forecast: {forecast}")
