"""CP1404/CP5632 Practical - UnreliableCar class"""

import random
from car import Car


class UnreliableCar(Car):
    """Specialised Car that sometimes does not drive."""

    def __init__(self, name, fuel, reliability):
        """Initialise a UnreliableCar with reliability percentage.

        reliability: float between 0 and 100
        """
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car only if a random number is less than reliability.

        Return the distance driven.
        """
        random_number = random.uniform(0, 100)
        if random_number < self.reliability:
            # It works this time - drive as normal
            return super().drive(distance)
        # Car does not move this time
        return 0

