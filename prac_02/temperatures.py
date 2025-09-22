"""CP1404/CP5632 Practical - Prac 02
Temperature conversion program with a simple menu.
"""
MENU = """    C)elsius to Fahrenheit
F)ahrenheit to Celsius
Q)uit
"""

def celsius_to_fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9

def main() -> None:
    print(MENU)
    choice = input(">>> ").strip().upper()
    while choice != "Q":
        try:
            if choice == "C":
                celsius = float(input("Celsius: "))
                print(f"Result: {celsius_to_fahrenheit(celsius):.2f} F")
            elif choice == "F":
                fahrenheit = float(input("Fahrenheit: "))
                print(f"Result: {fahrenheit_to_celsius(fahrenheit):.2f} C")
            else:
                print("Invalid option")
        except ValueError:
            print("Invalid input; enter a number.")
        print(MENU)
        choice = input(">>> ").strip().upper()
    print("Farewell.")

if __name__ == "__main__":
    main()
