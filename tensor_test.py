import tensorflow as tf
import pandas as pd
import numpy as np

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(20, activation='tanh'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

set_input = []
set_output = []

file = open('learning_set_SNN1.txt', 'r')
while True:
    line = file.readline()
    if not line:
        break
    x, y = map(int, line.split())
    set_input.append([x])
    set_output.append(y)

model.compile(optimizer='adam', loss = 'binary_crossentropy', metrics=['accuracy'])

file.close()

model.fit(np.array(set_input), np.array(set_output), epochs=100)

for i in range(1,101):
    expactation = model.predict([[i]])
    print(f"{i}\t: {expactation}")