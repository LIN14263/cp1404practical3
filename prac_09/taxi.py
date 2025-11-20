"""CP1404/CP5632 Practical - Taxi class example"""

from car import Car


class Taxi(Car):
    """Specialised version of a Car that includes fare costs."""
    price_per_km = 1.23  # class variable

    def __init__(self, name, fuel):
        """Initialise a Taxi instance, based on parent Car class."""
        super().__init__(name, fuel)
        self.current_fare_distance = 0

    def __str__(self):
        """Return a string like:
        'Prius 1, fuel=100, odometer=0, 0km on current fare, $1.23/km'
        """
        return (f"{super().__str__()}, {self.current_fare_distance}km on current fare, "
                f"${self.price_per_km:.2f}/km")

    def get_fare(self):
        """Calculate the price of the taxi trip.

        Fare is price_per_km * distance, rounded to nearest 10c.
        """
        fare = self.price_per_km * self.current_fare_distance
        # round to nearest 10c => 1 decimal place
        return round(fare, 1)

    def start_fare(self):
        """Begin a new fare."""
        self.current_fare_distance = 0

    def drive(self, distance):
        """Drive like parent Car, but also track fare distance."""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven

