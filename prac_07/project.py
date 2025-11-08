"""Project class for CP1404 prac_07 Project Management app."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, date

DATE_FMT = "%d/%m/%Y"  # e.g. 30/09/2020


@dataclass(order=True)
class Project:
    """Represent a project."""
    name: str
    start_date: date
    priority: int
    cost_estimate: float
    percent_complete: int

    @classmethod
    def from_csv(cls, row: list[str]) -> "Project":
        """Create a Project from a CSV row."""
        name, start_text, priority_text, cost_text, percent_text = row
        return cls(
            name=name.strip(),
            start_date=datetime.strptime(start_text.strip(), DATE_FMT).date(),
            priority=int(priority_text),
            cost_estimate=float(cost_text),
            percent_complete=int(percent_text),
        )

    def to_csv(self) -> list[str]:
        """Return list of strings for writing to CSV (with header elsewhere)."""
        return [
            self.name,
            self.start_date.strftime(DATE_FMT),
            str(self.priority),
            f"{self.cost_estimate:.2f}",
            str(self.percent_complete),
        ]

    def is_complete(self) -> bool:
        """Return True if project is 100% complete."""
        return self.percent_complete >= 100

    def __str__(self) -> str:
        status = "complete" if self.is_complete() else "incomplete"
        return (f"{self.name}, start: {self.start_date.strftime(DATE_FMT)}, "
                f"priority {self.priority}, estimate ${self.cost_estimate:,.2f}, "
                f"{self.percent_complete}% ({status})")
