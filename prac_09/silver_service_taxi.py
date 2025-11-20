"""CP1404/CP5632 Practical - SilverServiceTaxi class"""

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised Taxi with fanciness and flagfall."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi.

        fanciness: float that multiplies the base price_per_km.
        """
        super().__init__(name, fuel)
        self.fanciness = fanciness
        # customise this object's price_per_km based on class variable
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        """Return string including flagfall info."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Calculate the fare including flagfall."""
        return super().get_fare() + self.flagfall

