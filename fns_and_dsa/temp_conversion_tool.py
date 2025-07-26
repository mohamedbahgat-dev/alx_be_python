
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    temp_celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return temp_celsius

def convert_to_fahrenheit(celsius):
    temp_fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return temp_fahrenheit

temp = float(input("Enter the temperature to convert: "))
degree_type = input("Is this temperature in Celsius or Fahrenheit? ").upper()

if degree_type == 'F':
    print(f"{temp}°F is {convert_to_celsius(temp)}°C")
elif degree_type == 'C':
    print(f"{temp}°C is {convert_to_fahrenheit(temp)}°F")
else:
    print('Invaide input!')
