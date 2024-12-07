import numpy as np
import tensorflow as tf
from keras.layers import Dense, LSTM, Input, Embedding, Attention, GlobalAveragePooling1D
from keras.models import Model
from transformers import BertTokenizer, TFBertForSequenceClassification

def build_transformer_model(input_shape):
    inputs = Input(shape=input_shape)
    embedding = Embedding(input_dim=5000, output_dim=64)(inputs)
    attention = Attention()(embedding)
    pooled_output = GlobalAveragePooling1D()(attention)
    dense = Dense(64, activation='relu')(pooled_output)
    outputs = Dense(1, activation='sigmoid')(dense)
    model = Model(inputs, outputs)
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

def build_bert_model():
    model = TFBertForSequenceClassification.from_pretrained("bert-base-uncased")
    return model

def build_lstm_model(input_shape):
    model = tf.keras.Sequential()
    model.add(LSTM(50, return_sequences=True, input_shape=input_shape))
    model.add(LSTM(50))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

def train_model(model, data, labels):
    model.fit(data, labels, epochs=10, batch_size=32)
    return model

