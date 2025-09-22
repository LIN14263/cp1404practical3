"""CP1404/CP5632 - Practical 1
Shop calculator: read number of items, then their prices.
If total is over $100, apply 10% discount.
"""

DISCOUNT_RATE = 0.10
DISCOUNT_THRESHOLD = 100

def main():
    number_of_items = int(input("Number of items: "))
    while number_of_items < 0:
        print("Invalid number of items!")
        number_of_items = int(input("Number of items: "))

    total = 0.0
    for i in range(1, number_of_items + 1):
        price = float(input(f"Price of item {i}: $"))
        while price < 0:
            print("Price can't be negative.")
            price = float(input(f"Price of item {i}: $"))
        total += price

    if total > DISCOUNT_THRESHOLD:
        total *= (1 - DISCOUNT_RATE)

    print(f"Total price for {number_of_items} items is ${total:,.2f}")

if __name__ == "__main__":
    main()
