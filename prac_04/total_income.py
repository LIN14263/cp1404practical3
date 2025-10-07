"""
CP1404/CP5632 Practical 04 - Total income over given months
"""

def main():
    incomes = []
    month_count = get_positive_int("How many months? ")
    for month in range(1, month_count + 1):
        income = get_non_negative_float(f"Enter income for month {month}: ")
        incomes.append(income)

    print("\nIncome Report")
    print("-------------")
    total = 0.0
    for month, income in enumerate(incomes, start=1):
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f}  Total: ${total:10.2f}")

def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Enter a positive integer.")
        except ValueError:
            print("Invalid input; enter an integer.")

def get_non_negative_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            print("Enter a non-negative number.")
        except ValueError:
            print("Invalid input; enter a number.")

if __name__ == "__main__":
    main()
