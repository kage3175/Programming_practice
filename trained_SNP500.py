import tensorflow as tf
import pandas as pd
import numpy as np
import os

checkpoint_path = "training_1/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(30, activation='tanh'),
    tf.keras.layers.Dense(40, activation = 'tanh'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.load_weights(checkpoint_path)

input = [-0.03540097889 ,0.4473527, 1.2269018, 0.11706869999999998, -0.19683140000000002, -0.7922515, -0.286518, 0.24051189999999997, 0.6742215, 0.7411145, 0.847018, -0.1024381, 0.3855356, 0.7117288, 0.2357859, -0.6756875, 0.032415482690000004, 0.4034089156, 0.281471203, -0.01554474478]

expact = model.predict([input])

if expact > 0.9:
    print(f'증가, expact={expact[0][0]}')
elif expact > 0.5:
    print(f'아마도 증가, expact={expact[0][0]}')
elif expact > 0.1:
    print(f'아마도 감소, expact={expact[0][0]}')
else:
    print(f'감소, expact={expact[0][0]}')
#print(expact)