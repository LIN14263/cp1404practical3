"""
CP1404/CP5632 Assignment 1 – Books to Read 1.0
Program tuned to match the sample transcript (messages/prompts/ordering).
"""

from typing import List, Tuple

# ----- CONSTANTS (allowed globals) -----
FILENAME = "books.csv"
STATUS_UNREAD = "u"
STATUS_COMPLETED = "c"
MENU = (
    "Menu:\n"
    "D - Display books\n"
    "A - Add a new book\n"
    "C - Complete a book\n"
    "Q - Quit\n"
)
WELCOME_NAME = "Lindsay Ward"  # EXACTLY as in the transcript


def main() -> None:
    """Run the main program loop with exact prompts/messages."""
    print(f"Books to Read 1.0 by {WELCOME_NAME}")
    books = load_books(FILENAME)
    print(f"{len(books)} books loaded.")
    while True:
        print(MENU, end="")                   # show menu
        choice = input(">>> ").strip().lower()
        if choice == "d":
            display_books(books)
        elif choice == "a":
            add_book(books)
        elif choice == "c":
            complete_book(books)
        elif choice == "q":
            save_books(FILENAME, books)
            print(f"{len(books)} books saved to {FILENAME}")
            print('"So many books, so little time. Frank Zappa"')
            print("At the end of this run, the saved CSV file contained:")
            print_file_contents(FILENAME)     # print file content at the end (as in sample)
            break
        else:
            print("Invalid menu choice")


# ---------- File I/O ----------

def load_books(filename: str) -> List[List[str]]:
    """Load books from CSV into list of [title, author, pages_text, status]."""
    books: List[List[str]] = []
    try:
        with open(filename, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = [p.strip() for p in line.split(",")]
                if len(parts) != 4:
                    continue
                title, author, pages_text, status = parts
                if status not in (STATUS_UNREAD, STATUS_COMPLETED):
                    continue
                try:
                    int(pages_text)
                except ValueError:
                    continue
                books.append([title, author, pages_text, status])
    except FileNotFoundError:
        books = []
    return books


def save_books(filename: str, books: List[List[str]]) -> None:
    """Save books to CSV."""
    with open(filename, "w", encoding="utf-8") as f:
        for title, author, pages_text, status in books:
            f.write(f"{title},{author},{pages_text},{status}\n")


def print_file_contents(filename: str) -> None:
    """Print the file contents verbatim (used at quit, to match sample)."""
    try:
        with open(filename, encoding="utf-8") as f:
            for line in f:
                print(line.rstrip("\n"))
    except FileNotFoundError:
        pass


# ---------- Helpers ----------

def compute_unread_stats(books: List[List[str]]) -> Tuple[int, int]:
    """Return (total_pages_unread, count_unread)."""
    total_pages = 0
    count = 0
    for _, _, pages_text, status in books:
        if status == STATUS_UNREAD:
            total_pages += int(pages_text)
            count += 1
    return total_pages, count


def get_non_blank(prompt: str) -> str:
    """Prompt until a non-blank string is entered (exact message)."""
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("Input can not be blank")


def get_positive_int(prompt: str) -> int:
    """Prompt until a positive integer (> 0) is entered (exact messages)."""
    while True:
        text = input(prompt)
        try:
            value = int(text)
        except ValueError:
            print("Invalid input - please enter a valid number")
            continue
        if value <= 0:
            print("Number must be > 0")
            continue
        return value


# ---------- Display ----------

def display_books(books: List[List[str]]) -> None:
    """Display all books sorted by author then title, with '*' for unread and summary."""
    if not books:
        print("No books left to read. Why not add a new book?")
        return

    sorted_books = sorted(books, key=lambda b: (b[1].lower(), b[0].lower()))
    title_w = max((len(b[0]) for b in sorted_books), default=0)
    author_w = max((len(b[1]) for b in sorted_books), default=0)

    for i, (title, author, pages_text, status) in enumerate(sorted_books, start=1):
        marker = "*" if status == STATUS_UNREAD else " "
        print(f"{marker}{i}. {title:<{title_w}} by {author:<{author_w}} {int(pages_text):>4} pages")

    unread_pages, unread_count = compute_unread_stats(books)
    if unread_count > 0:
        print(f"You still need to read {unread_pages} pages in {unread_count} books.")
    else:
        print("No books left to read. Why not add a new book?")


# ---------- Menu actions ----------

def add_book(books: List[List[str]]) -> None:
    """Add a new unread book with validation and exact messages."""
    title = get_non_blank("Title: ")
    author = get_non_blank("Author: ")
    pages = get_positive_int("Number of Pages: ")
    books.append([title, author, str(pages), STATUS_UNREAD])
    print(f"{title} by {author} ({pages} pages) added.")


def complete_book(books: List[List[str]]) -> None:
    """Mark an unread book completed. Show list and summary first; exact errors."""
    if not any(b[3] == STATUS_UNREAD for b in books):
        print("No unread books - well done!")
        return

    sorted_books = sorted(books, key=lambda b: (b[1].lower(), b[0].lower()))
    title_w = max((len(b[0]) for b in sorted_books), default=0)
    author_w = max((len(b[1]) for b in sorted_books), default=0)

    for i, (title, author, pages_text, status) in enumerate(sorted_books, start=1):
        marker = "*" if status == STATUS_UNREAD else " "
        print(f"{marker}{i}. {title:<{title_w}} by {author:<{author_w}} {int(pages_text):>4} pages")

    unread_pages, unread_count = compute_unread_stats(books)
    print(f"You still need to read {unread_pages} pages in {unread_count} books.")
    print("Enter the number of a book to mark as completed")

    index = get_valid_book_number(len(sorted_books))
    sel_title, sel_author, sel_pages, sel_status = sorted_books[index - 1]
    if sel_status == STATUS_COMPLETED:
        print("That book is already completed")
        return
    for b in books:
        if b[0] == sel_title and b[1] == sel_author and b[2] == sel_pages:
            b[3] = STATUS_COMPLETED
            break
    print(f"{sel_title} by {sel_author} completed!")


def get_valid_book_number(max_index: int) -> int:
    """Prompt until a valid number in 1..max_index is entered with exact error messages."""
    while True:
        text = input(">>> ")
        try:
            value = int(text)
        except ValueError:
            print("Invalid input - please enter a valid number")
            continue
        if value <= 0:
            print("Number must be > 0")
            continue
        if value > max_index:
            print("Invalid book number")
            continue
        return value


if __name__ == "__main__":
    main()
