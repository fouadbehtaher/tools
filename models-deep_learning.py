from keras.models import Sequential
from keras.layers import LSTM, Dense
from sklearn.preprocessing import StandardScaler
import numpy as np
from transformers import BertModel, BertTokenizer
import torch

def build_lstm_model(input_shape):
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=input_shape))
    model.add(LSTM(units=50, return_sequences=False))
    model.add(Dense(units=1))  
    model.compile(optimizer='adam', loss='mean_squared_error')
    
    return model

def train_lstm_model(data):
    model = build_lstm_model(data.shape[1:])
    model.fit(data, data, epochs=100, batch_size=64)
    return model

def build_transformer_model(input_dim):
    model = Sequential()
    model.add(Dense(64, activation='relu', input_dim=input_dim))
    model.add(Dense(1, activation='sigmoid'))  # مثال على تحويل البيانات إلى 1
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    
    return model

def bert_analysis(texts):
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertModel.from_pretrained('bert-base-uncased')
    
    inputs = tokenizer(texts, return_tensors="pt", padding=True, truncation=True)
    outputs = model(**inputs)
    
    return outputs.last_hidden_state
