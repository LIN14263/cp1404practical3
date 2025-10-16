"""CP1404 Practical 5 - Wimbledon Champions
Reads 'wimbledon.csv' and shows champions and countries.
"""

import csv
from collections import Counter

CSV_FILENAME = "wimbledon.csv"


def load_wimbledon_records(filename):
    """Return list of (year, champion, country) from the CSV file."""
    records = []
    with open(filename, encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        next(reader, None)  # skip header
        for year, champion, country in reader:
            records.append((int(year), champion.strip(), country.strip()))
    return records


def main():
    try:
        records = load_wimbledon_records(CSV_FILENAME)
    except FileNotFoundError:
        print(f"Cannot find '{CSV_FILENAME}'. Place it in the same directory.")
        return

    champions = Counter(champion for _, champion, _ in records)
    countries = sorted({country for _, _, country in records})

    print("Wimbledon Champions")
    for name, count in sorted(champions.items(), key=lambda x: (-x[1], x[0])):
        print(f"{name:25} : {count}")

    print()
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))


if __name__ == "__main__":
    main()

