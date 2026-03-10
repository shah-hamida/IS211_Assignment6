class ConversionNotPossible(Exception):
    pass

def convert(fromUnit, toUnit, value):
    temperature = ["Celsius", "Fahrenheit", "Kelvin"]
    distance = ["Miles", "Yards", "Meters"]

    if fromUnit == toUnit:
        return value

    if fromUnit in temperature and toUnit in temperature:
        if fromUnit == "Celsius" and toUnit == "Fahrenheit":
            value = value * 9 / 5 + 32
            return value
        elif fromUnit == "Celsius" and toUnit == "Kelvin":
            value = value + 273.15
            return value
        elif fromUnit == "Fahrenheit" and toUnit == "Kelvin":
            value = value * 9 / 5- 32
            return value
        elif fromUnit == "Fahrenheit" and toUnit == "Celsius":
            value = value - 32 * 5/9
            return value
        elif fromUnit == "Kelvin" and toUnit == "Celsius":
            value = value - 273.15
            return value
        elif fromUnit == "Kelvin" and toUnit == "Fahrenheit":
            value = (value - 273.15) * 9 / 5 + 32
            return value

    if fromUnit in distance and toUnit in distance:
        if fromUnit == "Miles" and toUnit == "Yards":
            value = value * 1760
            return value
        elif fromUnit == "Miles" and toUnit == "Meters":
            value = value * 1609.34
            return value
        elif fromUnit == "Yards" and toUnit == "Meters":
            value = value * 0.9144
            return value
        elif fromUnit == "Yards" and toUnit == "Miles":
            value = value / 1760
            return value
        elif fromUnit == "Meters" and toUnit == "Miles":
            value = value / 1609.34
            return value
        elif fromUnit == "Meters" and toUnit == "Yards":
            value = value * 1.09361
            return value
    else:
        raise ConversionNotPossible("Error converting the Units")
