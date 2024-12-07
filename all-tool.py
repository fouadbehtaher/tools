from models.anomaly_detection import train_autoencoder, isolation_forest_anomaly_detection
from models.deep_learning import train_lstm_model
from models.time_series import prophet_analysis
from network_analysis.kafka_integration import consume_data_from_kafka
from alerts.prometheus_alerts import setup_prometheus_alerts, trigger_alert_if_needed
from cloud_integration.aws_integration import invoke_lambda
from security.mfa import enable_mfa_for_key_management

def main():
    print("تدريب نموذج Autoencoder...")

    print("تشغيل Kafka Integration...")

    print("التنبؤ باستخدام Prophet...")

if __name__ == "__main__":
    main()
