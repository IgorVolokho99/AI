import os

os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

import numpy as np
from tensorflow import keras
from tensorflow.keras.layers import Dense

c = np.array([-40, -10, 0, 8, 15, 22, 38])
f = np.array([-40, 14, 32, 46, 59, 72, 100])

model = keras.Sequential()
model.add(Dense(units=1, input_shape=(1,), activation="linear"))

model.compile(loss="mean_squared_error", optimizer=keras.optimizers.Adam(0.1))

history = model.fit(c, f, epochs=1000, verbose=False)

print(model.predict(np.array([100])))
