"""Temperature Converter Package.

A simple Python package for converting temperatures between Celsius, Fahrenheit, and Kelvin.
"""

__version__ = "1.0.0"
__author__ = "brucestudios"
__email__ = "bruce@example.com"

from .converter import celsius_to_fahrenheit, fahrenheit_to_celsius, celsius_to_kelvin, kelvin_to_celsius, fahrenheit_to_kelvin, kelvin_to_fahrenheit

__all__ = [
    "celsius_to_fahrenheit",
    "fahrenheit_to_celsius", 
    "celsius_to_kelvin",
    "kelvin_to_celsius",
    "fahrenheit_to_kelvin",
    "kelvin_to_fahrenheit",
]