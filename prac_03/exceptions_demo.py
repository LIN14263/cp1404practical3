# CP1404/CP5632 - Practical 03: Exceptions
# Get two integers and divide, handling invalid input and zero division.
# Always print "Finished." at the end.

def get_int(prompt: str) -> int:
    """Prompt until the user enters a valid integer."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")


def main():
    """Divide two integers with exception handling."""
    try:
        numerator = get_int("Numerator: ")
        denominator = get_int("Denominator: ")
        result = numerator / denominator
        print(f"{numerator} / {denominator} = {result}")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    finally:
        print("Finished.")


if __name__ == "__main__":
    main()
