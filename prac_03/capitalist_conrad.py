# CP1404/CP5632 - Practical: Capitalist Conrad
# Simulate a stock price that moves up/down by random percentages until it hits bounds.

import random

# ----- Constants (configuration) -----
START_PRICE = 10.0
MIN_PRICE = 1.0
MAX_PRICE = 100.0
MAX_INCREASE = 0.10   # 10% increase
MAX_DECREASE = 0.05   # 5% decrease
OUTPUT_FILE = "conrad_output.txt"


def simulate_price(start_price: float = START_PRICE) -> None:
    """Simulate daily price changes and write results to OUTPUT_FILE."""
    price = start_price
    day = 0

    with open(OUTPUT_FILE, "w", encoding="utf-8") as out_file:
        print(f"Starting price: ${price:,.2f}")
        print(f"Starting price: ${price:,.2f}", file=out_file)

        # Continue until price goes out of bounds
        while MIN_PRICE <= price <= MAX_PRICE:
            day += 1
            # 50/50 chance to increase or decrease
            if random.random() < 0.5:
                change = random.uniform(0, MAX_INCREASE)
            else:
                change = -random.uniform(0, MAX_DECREASE)

            price *= (1 + change)
            line = f"On day {day} price is ${price:,.2f}"
            print(line)
            print(line, file=out_file)


def main():
    """Run the Capitalist Conrad simulation."""
    # 可选：取消下一行注释以固定随机性，便于测试/标注
    # random.seed(0)
    simulate_price()


if __name__ == "__main__":
    main()
