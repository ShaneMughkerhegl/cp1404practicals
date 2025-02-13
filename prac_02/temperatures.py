# temperatures.py

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

# Main program
def main():
    # Convert Celsius to Fahrenheit
    celsius = float(input("Enter temperature in Celsius: "))
    print(f"{celsius}C is {celsius_to_fahrenheit(celsius):.2f}F")

    # Convert Fahrenheit to Celsius
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    print(f"{fahrenheit}F is {fahrenheit_to_celsius(fahrenheit):.2f}C")

# Call the main function to run the program
main()