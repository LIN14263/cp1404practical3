# language_file_reader.py
"""Read languages.csv and display language information."""
from programming_language import ProgrammingLanguage
import csv

FILENAME = "languages.csv"


def main():
    languages = load_languages(FILENAME)

    print("Languages:")
    for language in languages:
        print(f"  {language}")

    print("\nDynamically typed languages:")
    for language in languages:
        if language.is_dynamic():
            print(f"  {language.name}")


def load_languages(filename):
    """Load languages from CSV and return list of ProgrammingLanguage objects."""
    languages = []
    with open(filename, encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # skip header row
        for name, typing, reflection_text, year_text in reader:
            reflection = reflection_text.lower() == "true"
            year = int(year_text)
            languages.append(ProgrammingLanguage(name, typing, reflection, year))
    return languages


if __name__ == "__main__":
    main()
