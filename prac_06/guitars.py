"""
CP1404/CP5632 Practical 06 - Guitars client
Estimate: 20 minutes
Actual: (fill after running)
- Ask the user for guitars until a blank name.
- Store as Guitar objects, then display with indexing and "(vintage)" marker.
"""
from guitar import Guitar

def main():
    print("My guitars!")
    guitars = []

    # Input loop
    name = input("Name: ")
    while name.strip() != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost:,.2f} added.")
        name = input("Name: ")

    # Some starter data if none entered (optional for testing)
    if not guitars:
        guitars = [
            Guitar("Gibson L-5 CES", 1922, 16035.40),
            Guitar("Line 6 JTV-59", 2010, 1512.9),
        ]

    # Display
    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, start=1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar}{vintage_string}")

if __name__ == "__main__":
    main()
