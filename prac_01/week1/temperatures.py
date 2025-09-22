"""CP1404/CP5632 - Practical 1
Temperature converter with a simple menu:
C -> F and F -> C
"""

MENU = "(C)elsius to Fahrenheit\n(F)ahrenheit to Celsius\n(Q)uit"

def main():
    print(MENU)
    choice = input(">>> ").strip().upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = c_to_f(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = f_to_c(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").strip().upper()
    print("Thank you.")

def c_to_f(c: float) -> float:
    return c * 9 / 5 + 32

def f_to_c(f: float) -> float:
    return (f - 32) * 5 / 9

if __name__ == "__main__":
    main()
