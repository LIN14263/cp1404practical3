"""CP1404 Practical 5 - Emails
Collect users' emails and names into a dictionary, then display them.
- Guess the name from the email (before '@'), confirm/correct from user.
- Blank email to stop.
"""


def get_name_from_email(email: str) -> str:
    """Infer a 'Title Case' name from an email like 'first.last@domain' or 'first_last@...'.
    """
    username = email.split("@", 1)[0]
    # Replace common separators with spaces then title-case
    for sep in [".", "_", "-"]:
        username = username.replace(sep, " ")
    # Collapse multiple spaces and title case
    return " ".join(part for part in username.split() if part).title()


def main():
    email_to_name = {}

    email = input("Email: ").strip()
    while email:
        # Guess a name and confirm
        guessed_name = get_name_from_email(email)
        prompt = f"Is your name {guessed_name}? (Y/n) "
        is_correct = input(prompt).strip().lower()
        if is_correct == "n" or is_correct == "no":
            name = input("Name: ").strip().title()
        else:
            name = guessed_name
        email_to_name[email] = name
        email = input("Email: ").strip()

    # Print results
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


if __name__ == "__main__":
    main()

