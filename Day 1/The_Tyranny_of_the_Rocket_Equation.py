import math

def compute_fuel_quantity(mass):
    """Apply equation to compute fuels quantity"""
    return ( math.floor( int(mass) / 3 ) ) - 2

def compute_total_fuel(fuel_quantity):
    """fuel for the fuel quantity"""
    fuel_qtt = compute_fuel_quantity(fuel_quantity)
    tt_fuel_qtt = 0

    while fuel_qtt > 0:
        tt_fuel_qtt += fuel_qtt
        fuel_qtt = compute_fuel_quantity(fuel_qtt)
        
    return tt_fuel_qtt

if __name__ == "__main__":
    assert compute_fuel_quantity(12) == 2
    assert compute_fuel_quantity(14) == 2
    assert compute_fuel_quantity(1969) == 654
    assert compute_fuel_quantity(100756) == 33583

    assert compute_total_fuel(12) == 2
    assert compute_total_fuel(14) == 2
    assert compute_total_fuel(1969) == 966
    assert compute_total_fuel(100756) == 50346

    reponse = 0
    # Read input file
    with open("input.txt", "r") as input_file:

        for line in input_file:
            total_fuel_required = compute_total_fuel(line)
            reponse += total_fuel_required

        print(reponse)

        input_file.close()