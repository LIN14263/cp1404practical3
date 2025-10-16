"""CP1404 Practical 5 - Word Occurrences
Counts each word and prints aligned output sorted alphabetically.
"""

def main():
    text = input("Text: ").strip()
    words = text.split()
    counts = {}
    for word in words:
        word = word.lower()
        counts[word] = counts.get(word, 0) + 1

    items = sorted(counts.items())
    width = max((len(word) for word, _ in items), default=0)

    for word, count in items:
        print(f"{word:{width}} : {count}")


if __name__ == "__main__":
    main()
