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

print(set_input.pop())
print(set_output.pop())

model.compile(optimizer='adam', loss = 'binary_crossentropy', metrics=['accuracy'])
model.fit(np.array(set_input), np.array(set_output), epochs=300, callbacks=[cp_callback])
''', callbacks=[cp_callback]'''

input = [-0.448678, 1.1455777999999999, -0.035400999999999995, 0.4473527, 1.2269018, 0.11706869999999998, -0.19683140000000002, -0.7922515, -0.286518, 0.24051189999999997, 0.6742215, 0.7411145, 0.847018, -0.1024381, 0.3855356, 0.7117288, 0.2357859, -0.6756875, 0.032415482690000004, 0.004034089156]

expact = model.predict([input])

print(expact)
