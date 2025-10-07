"""
CP1404/CP5632 Practical 04 - Lists exercises
"""

NUM_COUNT = 5

def main():
    numbers = get_numbers(NUM_COUNT)
    print_results(numbers)
    usernames = [
        'jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
        'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
        'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface',
        'StartServer', 'bob'
    ]
    username = input("Username: ").strip()
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")

def get_numbers(n):
    """Prompt for n numbers and return them as a list of floats."""
    numbers = []
    for i in range(1, n + 1):
        while True:
            try:
                value = float(input(f"Number {i}: "))
                numbers.append(value)
                break
            except ValueError:
                print("Invalid input; enter a number.")
    return numbers

def print_results(numbers):
    """Print first, last, smallest, largest, and average values."""
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers):.2f}")

if __name__ == "__main__":
    main()
