# Fuzzy Logic Heater Control System

## Overview

This project implements a fuzzy logic controller for a simple heater system using Python and `scikit-fuzzy`.

The controller receives the current temperature as input and determines an appropriate heater power level between 0% and 100%.

Unlike a traditional rule-based system with strict thresholds, fuzzy logic allows smooth transitions between different temperature and heater-power levels.

## System Architecture

```text
Temperature Input
       ↓
   Fuzzification
       ↓
    Fuzzy Rules
       ↓
     Inference
       ↓
  Defuzzification
       ↓
 Heater Power (%)
```

## Input

The temperature variable ranges from 0°C to 20°C and contains three fuzzy sets:

- Very Cold
- Cold
- Almost Cold

## Output

The heater power ranges from 0% to 100% and contains three fuzzy sets:

- Low
- Medium
- High

## Fuzzy Rules

The controller uses the following rules:

```text
IF temperature is Very Cold
THEN heater power is High

IF temperature is Cold
THEN heater power is Medium

IF temperature is Almost Cold
THEN heater power is Low
```

## Membership Functions

Triangular membership functions are used for both the temperature and heater-power variables.

The overlapping membership functions allow the controller to produce gradual changes in heater power rather than abrupt changes.

## Example Inputs

The system is tested with the following temperatures:

```text
3°C
8°C
12°C
15°C
```

For each temperature, the controller calculates the corresponding heater power.

## Technologies

- Python
- NumPy
- scikit-fuzzy

## How to Run

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python main.py
```

The program prints the calculated heater power for each test temperature and displays the fuzzy membership functions.

## Project Structure

```text
fuzzy-heater-control/
├── README.md
├── main.py
└── requirements.txt
```

## Future Improvements

- Add more temperature categories.
- Introduce humidity as an additional input.
- Add a target/desired temperature.
- Implement a real-time control loop.
- Compare fuzzy control with traditional threshold-based control.
- Add visualization of the control surface.
