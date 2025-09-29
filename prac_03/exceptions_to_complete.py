# CP1404/CP5632 - Practical: Exceptions To Complete
# Starter code improved with complete exception handling.

def main():
    """Ask user for a valid score and convert to float safely."""
    score = get_valid_score()
    print(f"Your score is {score}")


def get_valid_score() -> float:
    """Prompt user until they enter a valid floating-point score between 0 and 100."""
    while True:  # for-loop 可以写成 while True + break
        try:
            score_text = input("Enter score (0-100): ")
            score = float(score_text)
            if 0 <= score <= 100:
                return score
            print("Score must be between 0 and 100 inclusive.")
        except ValueError:
            print("Invalid input; please enter a number.")


if __name__ == "__main__":
    main()
