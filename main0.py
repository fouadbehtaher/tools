import ssl_tools
import encryption_tools
import anomaly_detection
import data_visualization

def main():
    model = anomaly_detection.train_anomaly_detection_model()
    
    sample_input = [1, 0, 1, 0]  # بيانات للاختبار (افتراض آمن)
    
    security_status = anomaly_detection.predict_anomaly(model, sample_input)
    print(f"Security Status: {security_status}")
    
    data_visualization.plot_security_risk(security_status)
    
    data = "Sensitive Data"
    sha256_hash = encryption_tools.hash_sha256(data)
    print(f"SHA-256 Hash: {sha256_hash}")

    (public_key, private_key) = rsa.newkeys(512)
    encrypted_data = encryption_tools.rsa_encryption(data, public_key)
    print(f"Encrypted Data: {encrypted_data}")
    decrypted_data = encryption_tools.rsa_decryption(encrypted_data, private_key)
    print(f"Decrypted Data: {decrypted_data}")

if __name__ == "__main__":
    main()
