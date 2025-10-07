"""
CP1404/CP5632 Practical 04 - List Comprehensions
"""

def main():
    numbers = [1, 2, 3, 4, 5, 6, 7]
    print("Numbers:", numbers)

    # 1. Squares using list comprehension
    squares = [n * n for n in numbers]
    print("Squares:", squares)

    # Names and full names for comprehension tasks
    names = ["Bob", "Angel", "Jimi", "Alan", "Ada", "Ben"]
    full_names = ["Ada Lovelace", "Bob Timmons", "Alan Turing", "Grace Hopper"]

    # 2. Long names (>= 4)
    long_names = [name for name in names if len(name) >= 4]
    print("Long names (>=4):", long_names)

    # 3. Lowercase of all names
    lower_names = [name.lower() for name in names]
    print("Lowercase:", lower_names)

    # 4. Initials from full names
    initials = ["".join(part[0] for part in full_name.split()) for full_name in full_names]
    print("Initials:", initials)

    # 5. Names starting with 'A'
    a_names = [name for name in names if name.startswith('A')]
    print("Names starting with A:", a_names)

    # 6. Length of each name
    name_lengths = [len(name) for name in names]
    print("Name lengths:", name_lengths)

    # 7. Filter numbers greater than 5 from strings list
    strings = ["0", "3", "10", "20", "-2", "5", "7"]
    numbers_over_5 = [int(s) for s in strings if int(s) > 5]
    print("Numbers > 5:", numbers_over_5)

if __name__ == "__main__":
    main()

