from tensorflow.keras.layers import Dense, Dropout, LSTM
from tensorflow.keras.models import Sequential

# Neural Network
def lstm(train_shape):
  model = Sequential()
  model.add(LSTM(units=100, return_sequences=True, input_shape=(train_shape[1], 1)))
  model.add(Dropout(0.5))
  model.add(LSTM(units=50, return_sequences=True))
  model.add(Dropout(0.5))
  model.add(LSTM(units=25))
  model.add(Dropout(0.5))
  model.add(Dense(units=1))
  return model