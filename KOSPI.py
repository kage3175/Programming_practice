import tensorflow as tf
import pandas as pd
import numpy as np
import os

checkpoint_path = "training_2/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)
cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
                                                 save_weights_only=True,
                                                 verbose=1)

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(50, activation='tanh'),
    tf.keras.layers.Dense(50, activation = 'tanh'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

file = open("KOSPI.csv", "r")

input_set = []
set_input = []
set_output = []

for i in range(19):
    line = file.readline()
    x = float(line.replace(",", "").replace("\n", ""))
    input_set.append(x*100)

line = file.readline()
x, y = map(float, line.split(","))
input_set.append(x*100)

while True:
    line = file.readline()
    if not line:
        break
    x, y = map(float, line.split(","))
    input_set.pop(0)
    input_set.append(x*100)
    set_input.append(input_set.copy())
    set_output.append(y)

file.close()

model.compile(optimizer='adam', loss = 'binary_crossentropy', metrics=['accuracy'])
model.fit(np.array(set_input), np.array(set_output), epochs=250, callbacks=[cp_callback])
''', callbacks=[cp_callback]'''

input_set = [-0.6663077, -0.5526112, 0.5592113, 1.4893069, -0.3519733, -0.5518045, -0.8805739, -1.1571457, -0.2378587, 1.6578728, 0.47727020000000003, 0.6412348, 1.4305946999999999, -0.3538409, -0.434517, 0.0237765, -0.003071, 0.0036651, 0.0071922, 0.003016895375]

expact = model.predict(np.array([input_set]))

print(expact)
