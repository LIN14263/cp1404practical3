"""CP1404/CP5632 Practical - Prac 02
Score to result program.
Get a score from the user and print the result: Invalid/Bad/Passable/Excellent.
"""
from typing import Final

MIN_SCORE: Final[float] = 0.0
MAX_SCORE: Final[float] = 100.0

def classify_score(score: float) -> str:
    """Return a text classification for a numeric score [0, 100]."""
    if score < MIN_SCORE or score > MAX_SCORE:
        return "Invalid score"
    if score >= 90:
        return "Excellent"
    if score >= 50:
        return "Passable"
    return "Bad"

def main() -> None:
    try:
        score = float(input("Enter score: "))
    except ValueError:
        print("Invalid score")
        return
    print(classify_score(score))

if __name__ == "__main__":
    main()
