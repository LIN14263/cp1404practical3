"""CP1404/CP5632 Practical - Band class for association example"""


class Band:
    """Band class that contains a list of Musicians."""

    def __init__(self, name):
        """Initialise a Band with a name and empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string with the band name and musician details."""
        musician_strings = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musician_strings})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Ask each musician in the band to play."""
        for musician in self.musicians:
            musician.play()

