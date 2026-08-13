import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


def create_heater_system():
    """Create and return the fuzzy heater control system."""

    # Fuzzy variables
    temperature = ctrl.Antecedent(np.arange(0, 21, 1), "temperature")

    heater_power = ctrl.Consequent(np.arange(0, 101, 1), "heater_power")

    # Temperature membership functions
    temperature["very_cold"] = fuzz.trimf(temperature.universe, [0, 0, 10])

    temperature["cold"] = fuzz.trimf(temperature.universe, [5, 10, 15])

    temperature["almost_cold"] = fuzz.trimf(temperature.universe, [10, 15, 20])

    # Heater power membership functions
    heater_power["low"] = fuzz.trimf(heater_power.universe, [0, 25, 50])

    heater_power["medium"] = fuzz.trimf(heater_power.universe, [25, 50, 75])

    heater_power["high"] = fuzz.trimf(heater_power.universe, [50, 75, 100])

    # Fuzzy rules
    very_cold_rule = ctrl.Rule(temperature["very_cold"], heater_power["high"])

    cold_rule = ctrl.Rule(temperature["cold"], heater_power["medium"])

    almost_cold_rule = ctrl.Rule(temperature["almost_cold"], heater_power["low"])

    # Inference engine
    control_system = ctrl.ControlSystem([very_cold_rule, cold_rule, almost_cold_rule])

    return (ctrl.ControlSystemSimulation(control_system), temperature, heater_power)


def test_heater_system(heating, temperatures):
    """Test the heater system with the given temperatures."""

    for temperature_value in temperatures:
        heating.input["temperature"] = temperature_value
        heating.compute()

        heater_power_value = heating.output["heater_power"]

        print(
            f"Temperature = {temperature_value}°C "
            f"→ Heater Power = {heater_power_value:.2f}%"
        )


def main():
    """Run the fuzzy heater control system."""

    heating, temperature, heater_power = create_heater_system()

    temperatures = [3, 8, 12, 15]

    test_heater_system(heating, temperatures)

    temperature.view()
    heater_power.view(sim=heating)


if __name__ == "__main__":
    main()
