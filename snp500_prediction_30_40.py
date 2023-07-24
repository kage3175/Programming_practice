import tensorflow as tf
import pandas as pd
import numpy as np
import os

checkpoint_path = "training_1/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)
cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
                                                 save_weights_only=True,
                                                 verbose=1)

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(50, activation='tanh'),
    tf.keras.layers.Dense(50, activation = 'tanh'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

### 1에 가까울수록 상승할 확률이 높다

file = open("snp500.csv", "r")

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

set_input.pop()
set_output.pop()

model.compile(optimizer='adam', loss = 'binary_crossentropy', metrics=['accuracy'])
model.fit(np.array(set_input), np.array(set_output), epochs=300, callbacks=[cp_callback])
''', callbacks=[cp_callback]'''

print(input_set)

expact = model.predict(np.array([input_set]))

print(expact)
