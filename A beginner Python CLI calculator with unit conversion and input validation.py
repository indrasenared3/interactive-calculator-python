def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def km_to_miles(km):
    return km * 0.621371

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def get_valid_number(prompt):
    """Helper function with a while loop to ensure valid numeric input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    while True:
        print("\n==============================")
        print("   INTERACTIVE CALCULATOR     ")
        print("==============================")
        print("1. Basic Arithmetic (+, -, *, /)")
        print("2. Convert Kilometers to Miles")
        print("3. Convert Celsius to Fahrenheit")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ").strip()
        
        if choice == '1':
            print("\n--- Arithmetic Operations ---")
            print("Operations: +, -, *, /")
            op = input("Enter operator (+, -, *, /): ").strip()
            
            if op not in ('+', '-', '*', '/'):
                print("Invalid operator. Please try again.")
                continue
                
            num1 = get_valid_number("Enter first number: ")
            num2 = get_valid_number("Enter second number: ")
            
            if op == '+':
                result = add(num1, num2)
            elif op == '-':
                result = subtract(num1, num2)
            elif op == '*':
                result = multiply(num1, num2)
            elif op == '/':
                result = divide(num1, num2)
                
            print(f"Result: {result}")
            
        elif choice == '2':
            print("\n--- KM to Miles Conversion ---")
            km = get_valid_number("Enter distance in kilometers: ")
            miles = km_to_miles(km)
            print(f"{km} km is equal to {miles:.2f} miles.")
            
        elif choice == '3':
            print("\n--- Celsius to Fahrenheit Conversion ---")
            celsius = get_valid_number("Enter temperature in Celsius: ")
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C is equal to {fahrenheit:.2f}°F.")
            
        elif choice == '4':
            print("\nExiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 4.")

if __name__ == "__main__":
    main()