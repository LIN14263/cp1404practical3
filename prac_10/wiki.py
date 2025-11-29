"""
CP1404/CP5632 - Practical 10
wiki.py - simple file-based wiki helper functions.

Each page is stored as a .txt file inside the PAGES_DIRECTORY.
The filename is based on the page title.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import List

PAGES_DIRECTORY = Path("pages")
PAGE_EXTENSION = ".txt"


def _ensure_directory_exists() -> None:
    """Create the pages directory if it does not already exist."""
    PAGES_DIRECTORY.mkdir(parents=True, exist_ok=True)


def normalise_title(title: str) -> str:
    """Return a cleaned-up version of a title for use as a filename.

    - Strip leading/trailing whitespace
    - Replace internal spaces with underscores

    >>> normalise_title("  Hello World  ")
    'Hello_World'
    >>> normalise_title("simple-page")
    'simple-page'
    """
    return title.strip().replace(" ", "_")


def get_page_path(title: str) -> Path:
    """Return the full Path object for a page title."""
    _ensure_directory_exists()
    safe_title = normalise_title(title)
    return PAGES_DIRECTORY / f"{safe_title}{PAGE_EXTENSION}"


def list_pages() -> List[str]:
    """Return a sorted list of existing page titles (without .txt).

    >>> isinstance(list_pages(), list)
    True
    """
    _ensure_directory_exists()
    titles = []
    for file in PAGES_DIRECTORY.glob(f"*{PAGE_EXTENSION}"):
        titles.append(file.stem)
    return sorted(titles)


def page_exists(title: str) -> bool:
    """Return True if a page with this title exists."""
    return get_page_path(title).is_file()


def load_page(title: str) -> str:
    """Return the text content of the page with this title.

    Raises FileNotFoundError if the page does not exist.
    """
    path = get_page_path(title)
    if not path.is_file():
        raise FileNotFoundError(f"Page not found: {title!r}")
    return path.read_text(encoding="utf-8")


def save_page(title: str, content: str) -> None:
    """Save content as the given page title, overwriting any existing content."""
    path = get_page_path(title)
    path.write_text(content, encoding="utf-8")


def delete_page(title: str) -> None:
    """Delete the page with this title if it exists."""
    path = get_page_path(title)
    if path.is_file():
        path.unlink()


def search_pages(query: str) -> List[str]:
    """Return a list of page titles whose title or content contains the query (case-insensitive)."""
    query = query.strip().lower()
    if not query:
        return []

    matches = []
    for title in list_pages():
        content = load_page(title)
        if query in title.lower() or query in content.lower():
            matches.append(title)
    return matches


def main():
    """Simple command-line interface for quick manual testing."""
    _ensure_directory_exists()
    print("Simple Wiki (file-based)")
    print(f"Pages directory: {os.path.abspath(PAGES_DIRECTORY)}")

    while True:
        print("\n(L)ist  (V)iew  (E)dit  (D)elete  (Q)uit")
        choice = input("> ").strip().upper()

        if choice == "Q":
            break

        if choice == "L":
            titles = list_pages()
            if not titles:
                print("No pages yet.")
            else:
                for title in titles:
                    print(f"- {title}")
        elif choice == "V":
            title = input("Title: ")
            try:
                print(load_page(title))
            except FileNotFoundError:
                print("That page does not exist.")
        elif choice == "E":
            title = input("Title: ")
            try:
                old_content = load_page(title)
                print("Current content:\n")
                print(old_content)
                print("\nEnter new content (blank line to finish):")
            except FileNotFoundError:
                print("New page. Enter content (blank line to finish):")
                old_content = ""

            lines = []
            while True:
                line = input()
                if line == "":
                    break
                lines.append(line)
            new_content = "\n".join(lines)
            save_page(title, new_content)
            print("Saved.")
        elif choice == "D":
            title = input("Title to delete: ")
            delete_page(title)
            print("Deleted (if it existed).")
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
