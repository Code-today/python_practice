#temperature
def temperature_converter(amount, from_unit, to_unit):
    # Define conversion factors (relative to Celsius)
    conversion_factors = {
        'C': 1.0,   # Celsius
        'F': 1.8,   # Fahrenheit
        'K': 1.0    # Kelvin
    }

    # Check if the units are valid
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError("Invalid unit code")

    # Convert amount to Celsius first
    if from_unit == 'F':
        amount = (amount - 32) / 1.8
    elif from_unit == 'K':
        amount = amount - 273.15

    # Convert Celsius to the target unit
    if to_unit == 'F':
        converted_amount = amount * 1.8 + 32
    elif to_unit == 'K':
        converted_amount = amount + 273.15
    else:
        converted_amount = amount

    return converted_amount

# Example usage:
amount = float(input("Enter the temperature to convert: "))
from_unit = input("Enter the unit to convert from (C, F, K): ").upper()
to_unit = input("Enter the unit to convert to (C, F, K): ").upper()

converted_amount = temperature_converter(amount, from_unit, to_unit)
print(f"{amount} {from_unit} = {converted_amount:.2f} {to_unit}")
