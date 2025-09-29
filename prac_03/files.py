# CP1404/CP5632 - Practical 03: Files
# Tasks:
# 1) Prompt for a name; write to name.txt
# 2) Read name.txt and display it
# 3a) Read the first two ints from numbers.txt and print their sum
# 3b) Accumulator with for-loop: sum *all* ints in numbers.txt

NAME_FILE = "name.txt"
NUMBERS_FILE = "numbers.txt"


def write_name():
    """Ask the user for their name and write it to a file."""
    name = input("Name: ").strip()
    with open(NAME_FILE, "w", encoding="utf-8") as out_file:
        print(name, file=out_file)


def read_and_display_name():
    """Read the saved name and display it."""
    with open(NAME_FILE, "r", encoding="utf-8") as in_file:
        saved_name = in_file.read().strip()
    print(f"Your name is {saved_name}")


def sum_first_two_numbers():
    """Read the first two integers from numbers.txt and print their sum."""
    with open(NUMBERS_FILE, "r", encoding="utf-8") as in_file:
        first_line = in_file.readline()
        second_line = in_file.readline()
    first = int(first_line)
    second = int(second_line)
    print(first + second)


def sum_all_numbers():
    """Accumulator pattern using a for-loop to total all integers in numbers.txt."""
    total = 0
    with open(NUMBERS_FILE, "r", encoding="utf-8") as in_file:
        for line in in_file:          # for-loop performs repeated task (line by line)
            line = line.strip()
            if not line:
                continue
            try:
                number = int(line)
            except ValueError:
                # Skip lines that are not valid integers
                continue
            total += number           # accumulator
    print(total)


def main():
    """Run all file tasks in order."""
    write_name()
    read_and_display_name()
    sum_first_two_numbers()
    sum_all_numbers()


if __name__ == "__main__":
    main()
