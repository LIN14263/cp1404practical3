# CP1404/CP5632 - Practical: Password Checker
# Ask the user for a password, check its length, and print asterisks.

MIN_LENGTH = 4
MAX_LENGTH = 10


def main():
    """Prompt user for a valid password and print asterisks."""
    password = get_password(MIN_LENGTH, MAX_LENGTH)
    print_asterisks(password)


def get_password(min_length: int, max_length: int) -> str:
    """Prompt until the password is valid (length between min and max)."""
    password = input(f"Enter password ({min_length}-{max_length} characters): ")
    while len(password) < min_length or len(password) > max_length:
        print(f"Invalid password: must be between {min_length} and {max_length} characters.")
        password = input(f"Enter password ({min_length}-{max_length} characters): ")
    return password


def print_asterisks(password: str) -> None:
    """Print asterisks equal to the length of the password."""
    print("*" * len(password))


if __name__ == "__main__":
    main()
