# MNIST Handwritten Digit Classification

## Overview

This project implements a simple fully connected neural network for handwritten digit classification using the MNIST dataset.

The model takes a 28×28 grayscale image of a handwritten digit and predicts which digit it represents, from 0 to 9.

## Model Architecture

- Input: 784 features (28×28 pixels)
- Dense layer: 32 neurons, ReLU activation
- Dense layer: 64 neurons, ReLU activation
- Output layer: 10 neurons, Softmax activation

## Dataset

The project uses the built-in MNIST dataset provided by TensorFlow/Keras.

- 60,000 training images
- 10,000 test images
- Image size: 28×28
- Number of classes: 10

## Data Preprocessing

The images are:

1. Flattened from 28×28 pixels into 784 features.
2. Converted to `float32`.
3. Normalized from the range 0–255 to 0–1.

## Training Configuration

- Optimizer: Adam
- Loss function: Sparse Categorical Crossentropy
- Batch size: 64
- Epochs: 10
- Validation split: 10%

## Technologies

- Python
- TensorFlow
- Keras
- NumPy

## Results

Test accuracy:

**Replace this with your actual test accuracy after running the model.**

## How to Run

Clone the repository and install the dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python main.py
```

## Project Structure

```text
mnist-neural-network/
├── README.md
├── main.py
└── requirements.txt
```

## Future Improvements

- Replace the fully connected network with a Convolutional Neural Network (CNN).
- Add confusion matrix visualization.
- Add sample prediction visualizations.
- Experiment with different network architectures and hyperparameters.
