#train the simplest and quickest neural network --- IGNORE ---
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

# Create a simple neural network model
model = keras.Sequential([
    keras.layers.Dense(10, activation='relu', input_shape=(5,)),
    keras.layers.Dense(1)
])  

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')  

# Generate some dummy training data
x_train = np.random.rand(100, 5)
y_train = np.random.rand(100, 1)    

# Train the model
model.fit(x_train, y_train, epochs=5, batch_size=10)

loss = model.evaluate(x_train, y_train)
print(f"Training Loss: {loss}")

model.save("output/simple_neural_network_model")

history = model.fit(x_train, y_train, epochs=50, batch_size=10, validation_split=0.2)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.savefig("output/performance_graph.png")
