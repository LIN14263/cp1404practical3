"""CP1404/CP5632 Practical - Prac 02
Password stars program.
Ask for a password with a minimum length and print asterisks matching its length.
"""
MIN_LENGTH = 6

def get_password(min_length: int = MIN_LENGTH) -> str:
    """Prompt the user for a password of at least min_length characters and return it."""
    password = input(f"Password (at least {min_length} chars): ")
    while len(password) < min_length:
        print(f"Too short. Password must be at least {min_length} characters.")
        password = input(f"Password (at least {min_length} chars): ")
    return password

def print_asterisks(text: str) -> None:
    """Print asterisks equal to the length of text (no trailing newline change)."""
    print("*" * len(text))

def main() -> None:
    password = get_password()
    print_asterisks(password)

if __name__ == "__main__":
    main()
