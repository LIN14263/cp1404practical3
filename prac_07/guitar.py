# guitar.py
"""Guitar class used in CP1404 Practical 07."""
from datetime import date


class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        """Return the guitar's age in years."""
        return date.today().year - self.year

    def is_vintage(self):
        """Return True if the guitar is 50 or more years old."""
        return self.get_age() >= 50

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"
