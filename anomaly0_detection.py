import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def generate_synthetic_data():
    data = [
        [1, 0, 0, 1],  # آمن
        [0, 1, 1, 0],  # غير آمن
        [1, 1, 0, 1],  # آمن
        [0, 0, 1, 0],  # غير آمن
        [1, 0, 1, 1],  # آمن
        [0, 1, 0, 1],  # غير آمن
        [1, 1, 1, 0],  # غير آمن
        [0, 0, 0, 1],  # آمن
    ]
    labels = [1, 0, 1, 0, 1, 0, 0, 1]
    
    return np.array(data), np.array(labels)

def train_anomaly_detection_model():
    data, labels = generate_synthetic_data()
    
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)
    
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(8, activation='relu', input_shape=(X_train.shape[1],)),
        tf.keras.layers.Dense(4, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(X_train, y_train, epochs=20, batch_size=32, verbose=1)
    
    loss, accuracy = model.evaluate(X_test, y_test)
    print(f"Model Accuracy: {accuracy * 100:.2f}%")
    
    return model

def predict_anomaly(model, input_data):
    prediction = model.predict(np.array([input_data]))
    return "Anomaly Detected" if prediction > 0.5 else "Normal Behavior"
