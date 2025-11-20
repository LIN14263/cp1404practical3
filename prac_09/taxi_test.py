"""CP1404/CP5632 Practical - Taxi test"""

from taxi import Taxi


def main():
    """Test Taxi class."""
    my_taxi = Taxi("Prius 1", 100)

    # Drive 40 km
    my_taxi.drive(40)
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")

    # Restart meter and drive another 100 km
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")


if __name__ == "__main__":
    main()
