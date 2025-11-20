"""CP1404/CP5632 Practical - UnreliableCar tests"""

from unreliable_car import UnreliableCar


def main():
    """Test UnreliableCar over many drives."""
    reliable_car = UnreliableCar("Mostly Good", 100, 90)
    unreliable_car = UnreliableCar("Dodgy", 100, 30)

    for i in range(1, 13):
        print(f"Attempt {i}:")
        print(f"{reliable_car.name}: drove {reliable_car.drive(10)}km, "
              f"odo={reliable_car.odometer}, fuel={reliable_car.fuel}")
        print(f"{unreliable_car.name}: drove {unreliable_car.drive(10)}km, "
              f"odo={unreliable_car.odometer}, fuel={unreliable_car.fuel}")
        print()


if __name__ == "__main__":
    main()
