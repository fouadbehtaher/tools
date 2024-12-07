from keras.models import Sequential
from keras.layers import Dense

def build_dnn_model(input_dim):
    model = Sequential()
    model.add(Dense(units=64, activation='relu', input_dim=input_dim))
    model.add(Dense(units=32, activation='relu'))
    model.add(Dense(units=1, activation='sigmoid'))
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

def train_dnn_model(data, labels):
    model = build_dnn_model(data.shape[1])
    model.fit(data, labels, epochs=100, batch_size=32)
    return model
