import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as web
import datetime as dt

from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.layers import Dense, Dropout, LSTM
from tensorflow.keras.models import Sequential
from preprocess import scaling
from model import lstm
from predit import predict
from utils import visualize

crypto_currency = 'BTC'
against_currency = 'USD'

start = dt.datetime(2010, 1, 1)
end = dt.datetime.now()
data = web.DataReader(f'{crypto_currency}-{against_currency}', 'yahoo', start, end)

x_train, y_train = scaling(data)

model = lstm(x_train.shape)

model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(x_train, y_train, epochs=20, batch_size=32)

# Testing the model
test_start = dt.datetime(2010, 1, 1)
test_end = dt.datetime.now()

test_data = web.DataReader(f'{crypto_currency}-{against_currency}', 'yahoo', test_start, test_end)
actual_prices = test_data['Close'].values

total_dataset = pd.concat((data['Close'], test_data['Close']), axis=0)

model_inputs = total_dataset[len(total_dataset) - len(test_data) - prediction_days:].values
model_inputs = model_inputs.reshape(-1, 1)
model_inputs = scaler.fit_transform(model_inputs)

# Make prediction
prediction_prices = predict(model, prediction_days, model_inputs)

visualize(prediction_prices, actual_prices, crypto_currency)