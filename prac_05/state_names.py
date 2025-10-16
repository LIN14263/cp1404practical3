"""CP1404 Practical 5 - Dictionaries: State Names (EAFP version)
Accepts lower/upper/mixed-case abbreviations and prints all states aligned.
"""

STATES = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia",
}


def main():
    print("State Name Lookup")
    abbreviation = input("Enter short state: ").strip()
    while abbreviation:
        key = abbreviation.upper()
        try:
            print(f"{key} is {STATES[key]}")
        except KeyError:
            print("Invalid short state")
        abbreviation = input("Enter short state: ").strip()

    print("\nAll states:")
    max_key_len = max(len(k) for k in STATES)
    for key, name in STATES.items():
        print(f"{key:<{max_key_len}} is {name}")


if __name__ == "__main__":
    main()
