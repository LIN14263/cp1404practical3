"""
CP1404/CP5632 Practical 06 - Guitar class
Fields: name (str), year (int), cost (float)
Methods: get_age(current_year=2025), is_vintage()
"""
from __future__ import annotations
from dataclasses import dataclass

VINTAGE_AGE = 50

@dataclass
class Guitar:
    """Represent a Guitar with name, year and cost."""
    name: str
    year: int
    cost: float

    def __str__(self) -> str:
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self, current_year: int = 2025) -> int:
        """Return how old the guitar is in years."""
        return max(0, current_year - int(self.year))

    def is_vintage(self) -> bool:
        """Return True if the guitar is vintage (50 years or older)."""
        return self.get_age() >= VINTAGE_AGE
