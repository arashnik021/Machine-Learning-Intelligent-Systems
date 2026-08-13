# IMDB Sentiment Analysis with LSTM

## Overview

This project implements a sentiment analysis model using a Long Short-Term Memory (LSTM) neural network.

The model analyzes movie reviews from the IMDB dataset and predicts whether each review expresses a positive or negative sentiment.

## Task

This is a binary text classification problem:

```text
0 → Negative
1 → Positive
```

## Model Architecture

```text
Integer Word Sequence
        ↓
Embedding Layer
        ↓
LSTM (64 units)
        ↓
Dense (1 unit, Sigmoid)
        ↓
Positive / Negative
```

### Embedding Layer

The model uses an embedding dimension of 128 to transform word indices into learned numerical representations.

### LSTM Layer

The LSTM processes the sequence of words and learns relationships between words and their surrounding context.

### Output Layer

A sigmoid activation produces a value between 0 and 1 representing the predicted probability of positive sentiment.

## Dataset

The project uses the IMDB movie review dataset provided by TensorFlow/Keras.

- 25,000 training reviews
- 25,000 test reviews
- Vocabulary limited to the top 10,000 words
- Maximum sequence length: 100 words

## Data Preprocessing

Reviews are represented as sequences of integer word IDs.

To create a consistent input size, sequences are padded or truncated to 100 words using `pad_sequences`.

## Training Configuration

- Optimizer: Adam
- Loss function: Binary Crossentropy
- Batch size: 32
- Epochs: 5
- Validation split: 20%
- Vocabulary size: 10,000
- Embedding dimension: 128
- LSTM units: 64

## Technologies

- Python
- TensorFlow
- Keras
- NumPy

## Results

Test accuracy:

**Replace this with your actual test accuracy after running the model.**

## How to Run

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python main.py
```

The IMDB dataset will be downloaded automatically by TensorFlow/Keras when needed.

## Project Structure

```text
imdb-lstm-sentiment-analysis/
├── README.md
├── main.py
└── requirements.txt
```

## Future Improvements

- Increase the maximum review length.
- Experiment with Bidirectional LSTM.
- Add dropout layers to reduce overfitting.
- Compare LSTM with a GRU architecture.
- Add examples of positive and negative predictions.
