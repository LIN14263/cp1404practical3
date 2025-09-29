# CP1404/CP5632 - Practical 03: Randoms
# Demonstrate the random module and some experiments with ranges.

import random


def main():
    """Run random number demonstrations."""
    # Repeated task with for-loop: generate several samples each time
    for _ in range(3):
        print(random.randint(5, 20))        # line 1: int in [5, 20]
        print(random.randrange(3, 10, 2))   # line 2: odd int in {3,5,7,9}
        print(random.uniform(2.5, 5.5))     # line 3: float in [2.5, 5.5]
        print("-")

    # Extra: random int in [1, 100]
    print(random.randint(1, 100))


if __name__ == "__main__":
    main()

# -------------------------------------------------------------
# Q&A (for submission notes, not assessed by code):
# 1) line 1: integer between 5 and 20 inclusive; min=5, max=20
# 2) line 2: odd integer between 3 and 9; min=3, max=9; cannot be 4
# 3) line 3: float between 2.5 and 5.5; min=2.5, max=5.5

