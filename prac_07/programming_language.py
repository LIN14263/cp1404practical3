# programming_language.py
"""ProgrammingLanguage class for CP1404 Practical 07."""

class ProgrammingLanguage:
    """Represent a programming language."""

    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if language uses dynamic typing."""
        return self.typing.lower() == "dynamic"

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
