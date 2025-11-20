"""CP1404/CP5632 Practical - SilverServiceTaxi tests"""

from silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi."""
    hummer = SilverServiceTaxi("Hummer", 200, 4)
    hummer.drive(18)
    fare = hummer.get_fare()
    print(hummer)
    print(f"Fare for 18km trip = ${fare:.2f}")
    # from prac instructions: should be about $48.78, rounded to $48.80
    assert round(fare, 2) in (48.78, 48.80)


if __name__ == "__main__":
    main()
