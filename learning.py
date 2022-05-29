
import tensorflow as tf
import numpy as np

x = tf.keras.layers.Input(shape=[6])

h = tf.keras.layers.Dense(2)(x)
h = tf.keras.layers.BatchNormalization()(h)
h = tf.keras.layers.Activation('sigmoid')(h)

h = tf.keras.layers.Dense(2)(x)
h = tf.keras.layers.BatchNormalization()(h)
h = tf.keras.layers.Activation('sigmoid')(h)


y = tf.keras.layers.Dense(5, activation='sigmoid')(h)

model = tf.keras.models.Model(x, y)
model.compile(optimizer='adam', loss='mean_squared_error', metrics='accuracy')
model.fit(np.array(throwerInput), np.array(Toutput), epochs = 1000)
# #import tensorflow as tf
# import tensorflow as tf
# import numpy as np

# model = tf.keras.models.Sequential([
#                                     tf.keras.layers.Dense(8, activation='sigmoid'),
#                                     tf.keras.layers.BatchNormalization(),
#                                     tf.keras.layers.Dense(5, activation='sigmoid'),
#                                     tf.keras.layers.BatchNormalization(),
#                                     tf.keras.layers.Dense(1, activation='sigmoid')
# ])

# model.compile(optimizer='SGD', loss = 'mean_squared_error', metrics=['accuracy'])
# model.fit(np.array(hitterInput), np.array(hitterOutput), epochs = 1000)



import tensorflow as tf
import numpy as np

x = tf.keras.layers.Input(shape=[6])

h = tf.keras.layers.Dense(4)(x)
h = tf.keras.layers.BatchNormalization()(h)
h = tf.keras.layers.Activation('sigmoid')(h)


h = tf.keras.layers.Dense(2)(x)
h = tf.keras.layers.BatchNormalization()(h)
h = tf.keras.layers.Activation('sigmoid')(h)




# h = tf.keras.layers.Dense(64)(x)
# h = tf.keras.layers.BatchNormalization()(h)
# h = tf.keras.layers.Activation('sigmoid')(h)


# h = tf.keras.layers.Dense(128)(x)
# h = tf.keras.layers.BatchNormalization()(h)
# h = tf.keras.layers.Activation('sigmoid')(h)


y = tf.keras.layers.Dense(5, activation='sigmoid')(h)


