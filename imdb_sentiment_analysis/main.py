import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import LSTM, Dense, Embedding, Input
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Set parameters
max_features = 10_000  # Use only the top 10,000 words
maxlen = 100  # Limit each review to 100 words

# Load the IMDB dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.imdb.load_data(
    num_words=max_features
)

# Make all reviews the same length
x_train = pad_sequences(x_train, maxlen=maxlen)
x_test = pad_sequences(x_test, maxlen=maxlen)

# Build the neural network
model = Sequential(
    [
        Input(shape=(maxlen,)),
        Embedding(input_dim=max_features, output_dim=128),
        LSTM(64),
        Dense(1, activation="sigmoid"),
    ]
)

# Configure how the model learns
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

# Train the model
model.fit(x_train, y_train, epochs=5, batch_size=32, validation_split=0.2, verbose=2)

# Evaluate the model on the test set
test_loss, test_accuracy = model.evaluate(x_test, y_test, verbose=2)

print(f"Test Accuracy: {test_accuracy * 100:.2f}%")
