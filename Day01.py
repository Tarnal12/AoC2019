import math


def get_fuel_req(initial_mass, include_compound_fuel):
    initial_mass = int(initial_mass)
    fuel_req = math.floor(initial_mass / 3.0)
    fuel_req = fuel_req - 2

    if fuel_req <= 0:
        return 0

    if include_compound_fuel:
        return fuel_req + get_fuel_req(fuel_req, True)
    else:
        return fuel_req


def run(include_compound_fuel):
    with open('Day01Input.txt') as input_file:
        total_fuel = 0
        for line in input_file:
            total_fuel = total_fuel + get_fuel_req(line, include_compound_fuel)

    print("Fuel for components (ignoring fuel requirements) = %d" % total_fuel)


run(False)
run(True)
