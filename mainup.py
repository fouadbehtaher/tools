import rsa
from encryption_tools import rsa_encrypt_with_aes_and_chacha, rsa_decrypt_with_aes_and_chacha, generate_kms_key, encrypt_with_kms, decrypt_with_kms
from anomaly_detection import train_xgboost_model, train_isolation_forest, real_time_alert
from network_analysis import network_anomaly_detection, network_anomaly_detection_with_xgboost

(public_key, private_key) = rsa.newkeys(2048)

data = "This is a sensitive message"
encrypted_aes_key, encrypted_chacha_key, aes_encrypted_data, chacha_encrypted_data = rsa_encrypt_with_aes_and_chacha(data, public_key)
decrypted_aes_data, decrypted_chacha_data = rsa_decrypt_with_aes_and_chacha(encrypted_aes_key, encrypted_chacha_key, aes_encrypted_data, chacha_encrypted_data, private_key)

print("Decrypted AES Data:", decrypted_aes_data)
print("Decrypted ChaCha20 Data:", decrypted_chacha_data)

key_id = generate_kms_key()
encrypted_data = encrypt_with_kms(data, key_id)
decrypted_data = decrypt_with_kms(encrypted_data, key_id)
print(f"Decrypted Data from KMS: {decrypted_data}")

model = train_xgboost_model()

input_data = [1, 0, 0, 1]
prediction = predict_anomaly(model, input_data)
print(f"Prediction for input data {input_data}: {prediction}")

isolation_predictions = train_isolation_forest()
real_time_alert(isolation_predictions)

network_data = [
    [1, 0, 0, 1],
    [0, 1, 1, 0],
    [1, 1, 0, 1],
    [0, 0, 1, 0],
    [1, 0, 1, 1],
]
network_predictions = network_anomaly_detection(network_data)
print(f"Network Anomaly Detection Predictions: {network_predictions}")

network_predictions_with_xgboost = network_anomaly_detection_with_xgboost(network_data)
print(f"Network Anomaly Detection with XGBoost: {network_predictions_with_xgboost}")
