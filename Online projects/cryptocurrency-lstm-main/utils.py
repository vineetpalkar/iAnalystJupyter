import numpy as np
import matplotlib.pyplot as plt

# Visualize the prices
def visualize (predicted, actual, crypto):
  plt.plot(actual, color='black', label='Actual Prices')
  plt.plot(predicted, color='red', label='Predicted Prices')
  plt.title(f'{crypto} Price Prediction')
  plt.xlabel('Time')
  plt.ylabel('Price')
  plt.legend(loc='upper left')
  plt.show()  