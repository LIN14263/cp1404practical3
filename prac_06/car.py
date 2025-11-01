"""
CP1404/CP5632 Practical 06 - Classes
Car class with a name, fuel amount and odometer.
Includes __str__, add_fuel and drive methods.
"""
from __future__ import annotations

class Car:
    """Represent a Car object."""

    def __init__(self, name: str = "Car", fuel: float = 0.0):
        """Initialise a Car instance.
        name: reference name for the car
        fuel: float, one unit of fuel drives one kilometre
        """
        self.name = name
        self.fuel = float(fuel)
        self.odometer = 0.0

    def __str__(self) -> str:
        """Return string representation of the car with name, fuel and odometer."""
        return f"{self.name}, fuel={int(self.fuel)}, odometer={int(self.odometer)}"

    def add_fuel(self, amount: float) -> None:
        """Add amount to the car's fuel."""
        if amount < 0:
            raise ValueError("Cannot add negative fuel")
        self.fuel += amount

    def drive(self, distance: float) -> float:
        """Drive the car a given distance if it has enough fuel.
        Drive as far as fuel allows, and return the actual distance driven.
        """
        if distance < 0:
            raise ValueError("Distance must be >= 0")

        distance_driven = min(distance, self.fuel)
        self.fuel -= distance_driven
        self.odometer += distance_driven
        return distance_driven
