"""
CP1404/CP5632 Practical 04 - Quick Picks (Lotto)
Generate lines of 6 unique numbers (1..45) sorted ascending, width=2
"""

import random

NUMBERS_PER_PICK = 6
MIN = 1
MAX = 45

def main():
    pick_count = get_positive_int("How many quick picks? ")
    for _ in range(pick_count):
        line = sorted(random.sample(range(MIN, MAX + 1), NUMBERS_PER_PICK))
        print(" ".join(f"{n:2d}" for n in line))

def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Enter a positive integer.")
        except ValueError:
            print("Invalid input; enter an integer.")

if __name__ == "__main__":
    main()
