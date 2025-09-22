"""CP1404/CP5632 Practical - Prac 02
Menu-based score program using functions.
Options:
(G)et result - show the textual result for your score
(S)how stars - print as many '*' as the integer part of your score
(R)andom score - generate a random score and show its result
(Q)uit
"""
import random
from typing import Final

MIN_SCORE: Final[float] = 0.0
MAX_SCORE: Final[float] = 100.0

MENU = """    G)et result
S)how stars
R)andom score
Q)uit
"""

def classify_score(score: float) -> str:
    """Return a text classification for a numeric score [0, 100]."""
    if score < MIN_SCORE or score > MAX_SCORE:
        return "Invalid score"
    if score >= 90:
        return "Excellent"
    if score >= 50:
        return "Passable"
    return "Bad"

def get_score() -> float:
    """Prompt for a valid score in [0, 100] and return it."""
    while True:
        try:
            score = float(input("Score (0-100): "))
            if MIN_SCORE <= score <= MAX_SCORE:
                return score
            print("Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input; enter a number.")

def show_stars(score: float) -> None:
    """Print stars equal to the integer part of score."""
    print("*" * int(score))

def main() -> None:
    score = get_score()
    print(MENU)
    choice = input(">>> ").strip().upper()
    while choice != "Q":
        if choice == "G" or choice == "GET RESULT":
            print(classify_score(score))
        elif choice == "S" or choice == "SHOW STARS":
            show_stars(score)
        elif choice == "R" or choice == "RANDOM SCORE":
            score = random.randint(0, 100)
            print(f"Random score: {score} -> {classify_score(score)}")
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").strip().upper()
    print("Farewell.")

if __name__ == "__main__":
    main()
