"""CP1404 Practical 5 - Dictionaries: Hex Colour Lookup (case-insensitive)"""

COLOUR_TO_HEX = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "bisque": "#ffe4c4",
    "black": "#000000",
    "blueviolet": "#8a2be2",
    "coral": "#ff7f50",
}


def main():
    print("Hex Colour Lookup (blank to quit)")
    while True:
        name = input("Colour name: ").strip()
        if not name:
            break
        key = name.lower()
        try:
            print(COLOUR_TO_HEX[key])
        except KeyError:
            print("Invalid colour name")


if __name__ == "__main__":
    main()

