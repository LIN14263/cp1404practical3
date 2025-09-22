"""CP1404/CP5632 - Practical 1
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the bonus rate is 10%; otherwise 15%.
Keep asking for sales until a negative number is entered.
"""

BONUS_LOW_RATE = 0.10
BONUS_HIGH_RATE = 0.15
THRESHOLD = 1000

def main():
    sales = float(input("Enter sales: $"))
    while sales >= 0:
        rate = BONUS_LOW_RATE if sales < THRESHOLD else BONUS_HIGH_RATE
        bonus = sales * rate
        print(f"Bonus: ${bonus:,.2f}")
        sales = float(input("Enter sales: $"))
    print("Done.")

if __name__ == "__main__":
    main()
