import xgboost as xgb
from sklearn.model_selection import train_test_split

def xgboost_anomaly_detection(data, labels):
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)
    
    model = xgb.XGBClassifier(use_label_encoder=False)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    return y_pred
