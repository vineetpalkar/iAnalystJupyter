import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as web
import datetime as dt

from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.layers import Dense, Dropout, LSTM
from tensorflow.keras.models import Sequential
from preprocess import preprocess

def predict(model, num_days, inputs):
  x_test = []

  for x in range(num_days, len(inputs)):
      x_test.append(inputs[x - num_days : x, 0])

  x_test = np.array(x_test)
  x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

  prediction_prices = model.predict(x_test)
  prediction_prices = scaler.inverse_transform(prediction_prices)

  # Predict next day
  real_data = [model_inputs[len(model_inputs) + 1 - prediction_days : len(model_inputs) + 1, 0]]
  real_data = np.array(real_data)
  real_data = np.reshape(real_data, (real_data.shape[0], real_data.shape[1], 1))

  prediction = model.predict(real_data)
  prediction = scaler.inverse_transform(prediction)
  print('Tomorrow\'s price will be: $', round(prediction[0][0], 2))

  return prediction_prices