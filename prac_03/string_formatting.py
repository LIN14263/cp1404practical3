# CP1404/CP5632 - Practical 03: String Formatting
# Demonstrate string formatting styles and aligned numeric output.

GUITAR_NAME = "Gibson L-5 CES"
FIRST_YEAR = 1922
ESTIMATED_COST = 16035.4


def main():
    """Show different formatting approaches and aligned columns."""
    # Old-style (for comparison)
    print("My guitar: %s, first made in %d" % (GUITAR_NAME, FIRST_YEAR))

    # str.format
    print("My guitar: {}, first made in {}".format(GUITAR_NAME, FIRST_YEAR))
    print("My {0} was first made in {1}".format(GUITAR_NAME, FIRST_YEAR))
    print("My {0} was first made in {1} (yeah, {1}!)".format(GUITAR_NAME, FIRST_YEAR))

    # f-strings (preferred)
    print(f"My {GUITAR_NAME} was first made in {FIRST_YEAR} (yeah, {FIRST_YEAR}!)")
    print(f"My {GUITAR_NAME} would cost ${ESTIMATED_COST:,.2f}")

    # Repeated task with for-loop; right-aligned integers in width 5
    numbers = [1, 19, 123, 456, -25]
    for index, number in enumerate(numbers, start=1):
        print(f"Number {index} is {number:>5}")


if __name__ == "__main__":
    main()

