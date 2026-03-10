from conversions import (convertCelsiusToKelvin, convertFahrenheitToCelsius,
                         convertFahrenheitToKelvin, convertCelsiusToFahrenheit, convertKelvinToFahrenheit,
                         convertKelvinToCelsius)
from conversions_refactored import convert

# converting Celsius to Kelvin and testing five test
print("Celsius to Kelvin")
print(convertCelsiusToKelvin(50), "First Test")
print(convertCelsiusToKelvin(150), "Second Test")
print(convertCelsiusToKelvin(0), "Third Test")
print(convertCelsiusToKelvin(100), "Fourth Test")
print(convertCelsiusToKelvin(200), "Fifth Test")

# converting Celsius to Fahrenheit and testing five test
print("")
print("Celsius to Fahrenheit")
print(convertCelsiusToFahrenheit(60), "First Test")
print(convertCelsiusToFahrenheit(140), "Second Test")
print(convertCelsiusToFahrenheit(0), "Third Test")
print(convertCelsiusToFahrenheit(100), "Fourth Test")
print(convertCelsiusToFahrenheit(200), "Fifth Test")

# converting Fahrenheit to Celsius and testing five test
print("")
print("Fahrenheit to Celsius")
print(convertFahrenheitToCelsius(100), "First Test")
print(convertFahrenheitToCelsius(140), "Second Test")
print(convertFahrenheitToCelsius(0), "Third Test")
print(convertFahrenheitToCelsius(200), "Fourth Test")
print(convertFahrenheitToCelsius(170), "Fifth Test")

print("")
print("Fahrenheit to Kelvin")
print(convertFahrenheitToKelvin(0), "First Test")
print(convertFahrenheitToKelvin(140), "Second Test")
print(convertFahrenheitToKelvin(100), "Third Test")
print(convertFahrenheitToKelvin(200), "Fourth Test")
print(convertFahrenheitToKelvin(150), "Fifth Test")

print("")
print("Kelvin to Fahrenheit")
print(convertKelvinToFahrenheit(50), "First Test")
print(convertKelvinToFahrenheit(140), "Second Test")
print(convertKelvinToFahrenheit(0), "Third Test")
print(convertKelvinToFahrenheit(100), "Fourth Test")
print(convertKelvinToFahrenheit(180), "Fifth Test")

print("")
print("Kelvin to Celsius")
print(convertKelvinToCelsius(80), "First Test")
print(convertKelvinToCelsius(140), "Second Test")
print(convertKelvinToCelsius(0), "Third Test")
print(convertKelvinToCelsius(100), "Fourth Test")
print(convertKelvinToCelsius(180), "Fifth Test")
print("")

# check that all the temperature and distance conversions is working correctly
print(convert("Celsius", "Kelvin", 100))
print(convert("Celsius", "Fahrenheit", 150))
print(convert("Kelvin", "Fahrenheit", 180))
print(convert("Kelvin", "Celsius", 200))
print(convert("Fahrenheit", "Celsius", 100))
print(convert("Fahrenheit", "Kelvin", 180))
print("")
print(convert("Miles", "Yards", 2))
print(convert("Miles", "Meters", 20))
print(convert("Meters", "Yards", 14))
print(convert("Meters", "Miles", 9))
print(convert("Miles", "Yards", 5))
print(convert("Miles", "Meters", 6))

# check if the exception will raise
print(convert("Kelvin", "Yards", 4))