"""
CP1404/CP5632 Practical 06 - ProgrammingLanguage class
Fields: name, typing ("Dynamic"/"Static"), reflection (bool), year (int)
"""
from __future__ import annotations

class ProgrammingLanguage:
    """Store details for a programming language."""

    def __init__(self, name: str, typing: str, reflection: bool, year: int):
        self.name = name
        self.typing = typing  # "Dynamic" or "Static"
        self.reflection = bool(reflection)
        self.year = int(year)

    def __str__(self) -> str:
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self) -> bool:
        """Return True if this language is dynamically typed."""
        return self.typing.strip().lower() == "dynamic"
