"""CP1404/CP5632 - Practical 1
Get a score (0-100) and print its status:
- Excellent: >= 90
- Passable: 50..89
- Bad: < 50
Also show a random score example.
"""

import random

def main():
    score = float(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score (0-100): "))

    print(grade_for(score))

    random_score = random.uniform(0, 100)
    print(f"Random score: {random_score:.2f} -> {grade_for(random_score)}")

def grade_for(score: float) -> str:
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

if __name__ == "__main__":
    main()
