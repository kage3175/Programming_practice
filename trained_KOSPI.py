import tensorflow as tf
import pandas as pd
import numpy as np
import os

checkpoint_path = "training_2/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(30, activation='tanh'),
    tf.keras.layers.Dense(40, activation = 'tanh'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.load_weights(checkpoint_path)

input = [-0.5526112, 0.5592113, 1.4893069, -0.3519733, -0.5518045, -0.8805739, -1.1571457, -0.2378587, 1.6578728, 0.47727020000000003, 0.6412348, 1.4305946999999999, -0.3538409, -0.434517, 0.0237765, -0.3071, 0.36651, 0.71922, 0.3016895375, -1.672697481]

expact = model.predict([input])

print(expact)