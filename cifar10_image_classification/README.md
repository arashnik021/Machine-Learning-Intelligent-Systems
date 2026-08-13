# CIFAR-10 Image Classification

## Overview

This project implements a fully connected neural network for image classification using the CIFAR-10 dataset and TensorFlow/Keras.

The model classifies color images into one of 10 object categories.

## Dataset

The CIFAR-10 dataset contains 60,000 color images divided into 10 classes.

* 50,000 training images
* 10,000 test images
* Image size: 32×32×3
* Number of classes: 10

The classes are:

```text
airplane
automobile
bird
cat
deer
dog
frog
horse
ship
truck
```

## Model Architecture

```text
Input: 32×32×3
      ↓
Flatten
      ↓
Dense: 512 neurons, ReLU
      ↓
Dense: 256 neurons, ReLU
      ↓
Dense: 128 neurons, ReLU
      ↓
Dense: 10 neurons, Softmax
```

## Data Preprocessing

Pixel values are converted from integers in the range 0–255 to floating-point values in the range 0–1.

## Training Configuration

* Optimizer: Adam
* Loss function: Sparse Categorical Crossentropy
* Batch size: 64
* Epochs: 20
* Validation split: 20%

## Technologies

* Python
* TensorFlow
* Keras
* NumPy

## Results

Test accuracy:

**Replace this with your actual test accuracy after running the model.**

## How to Run

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the model:

```bash
python main.py
```

## Project Structure

```text
cifar10-image-classification/
├── README.md
├── main.py
└── requirements.txt
```

## Future Improvements

* Implement a CNN architecture.
* Add data augmentation.
* Visualize training and validation accuracy.
* Generate a confusion matrix.
* Compare the fully connected model with a CNN.
