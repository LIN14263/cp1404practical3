"""
CP1404/CP5632 Practical 06 - Classes (Car walkthrough and modifications)
- Create 'limo' with 100 units of fuel
- Add 20 fuel
- Print current fuel
- Attempt to drive 115 km
- Ensure __str__ with name is used
"""
from car import Car

def main():
    # Existing demo car
    my_car = Car("My car", 180)
    my_car.drive(30)
    print(my_car)

    # 1. Create a new Car object called "limo" initialised with 100 units of fuel.
    limo = Car("Limo", 100)

    # 2. Add 20 more units of fuel.
    limo.add_fuel(20)

    # 3. Print the amount of fuel in the car.
    print(f"Limo fuel: {int(limo.fuel)}")

    # 4. Attempt to drive the car 115 km.
    distance_driven = limo.drive(115)
    print(f"Limo attempted to drive 115km, actually drove {int(distance_driven)}km")

    # 7. Print car object(s) to ensure __str__ works.
    print(limo)

if __name__ == "__main__":
    main()
