import copy
from typing import List, Dict, NamedTuple, Tuple
import numpy as np
from itertools import permutations
import math

class Coordinates:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def energy(self):
        return abs(self.x) + abs(self.y) + abs(self.z) 

    def __eq__(self, pos):
        return self.x==pos.x and self.y==pos.y and self.z==pos.z

    def __repr__(self):
        return "pos=<x={x}, y={y}, z={z}>".format(x=str(self.x), y=str(self.y), z=str(self.z))

def parse_input(input_file) -> List[Coordinates]:
    moons_pos_str = input_file.split("\n")
    return  [parse_position(moon) for moon in moons_pos_str]

def parse_position(pos_str: str) -> Coordinates:
    pos = pos_str[1:-1].split(", ")
    return Coordinates(int(pos[0][2:]), int(pos[1][2:]), int(pos[2][2:]))

def gravity(m1, m2) -> Tuple[int, int, int]:
    if m1.x == m2.x:
        x = 0
    elif m1.x < m2.x:
        x = 1
    else:
        x = -1
    
    if m1.y == m2.y:
        y = 0
    elif m1.y < m2.y:
        y = 1
    else:
        y = -1
    
    if m1.z == m2.z:
        z = 0
    elif m1.z < m2.z:
        z = 1
    else:
        z = -1

    return x, y, z

def apply_velocity(pos, vel) -> Coordinates:
    """update position by applying velocity"""
    pos.x += vel.x
    pos.y += vel.y
    pos.z += vel.z
    return pos

def apply_gravity(moons, velocity) -> Tuple[List[Coordinates], List[Coordinates]]:
    
    for permut in permutations(range(4), 2):
        moon1_idx = permut[0] 
        moon2_idx = permut[1]
        x_vel, y_vel, z_vel = gravity(moons[moon1_idx], moons[moon2_idx])
        velocity[int(moon1_idx)].x += x_vel
        velocity[int(moon1_idx)].y += y_vel
        velocity[int(moon1_idx)].z += z_vel

    return [apply_velocity(moon, vel) for moon, vel in zip(moons, velocity)], velocity

def run(step, moons):
    velocity = [Coordinates(0,0,0) for _ in range(4)]
    for _ in range(step):
        moons, velocity = apply_gravity(moons, velocity)
    return moons, velocity

def compute_energy(moons, velocity) -> int:
    return sum([moon.energy() * vel.energy() for moon, vel in zip(moons, velocity)])

def get_energy(steps, moons):
    moons, velocity = run(steps, moons)
    return compute_energy(moons,velocity)

def runx(moons):
    velocity = [Coordinates(0,0,0) for _ in range(4)]

    moons_initial_state = copy.deepcopy(moons)
    init_pos = [moon.x for moon in moons_initial_state]
    count = 0
    while True:

        moons, velocity = apply_gravity(moons, velocity)
        count += 1
        if [moon.x for moon in moons] == init_pos and [vel.x for vel in velocity] == [0, 0, 0, 0]:
            break

    return count

def runy(moons):
    velocity = [Coordinates(0,0,0) for _ in range(4)]

    moons_initial_state= copy.deepcopy(moons)
    init_pos = [moon.y for moon in moons_initial_state]
    count = 0
    while True:

        moons, velocity = apply_gravity(moons, velocity)
        count += 1
        if [moon.y for moon in moons] == init_pos and [vel.y for vel in velocity] == [0, 0, 0, 0]:
            break

    return count

def runz(moons):
    velocity = [Coordinates(0,0,0) for _ in range(4)]

    moons_initial_state = copy.deepcopy(moons)
    init_pos = [moon.z for moon in moons_initial_state]
    count = 0
    while True:

        moons, velocity = apply_gravity(moons, velocity)
        count += 1
        
        if [moon.z for moon in moons] == init_pos and [vel.z for vel in velocity] == [0, 0, 0, 0]:
            break

    return count

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

if __name__ == "__main__":
    TEST_CASE = """<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>"""
    TEST_STEP = 10
    moons_test = parse_input(TEST_CASE)
    print(get_energy(TEST_STEP, copy.deepcopy(moons_test)))

    TEST_CODE = """<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>"""

    moons_test_2 = parse_input(TEST_CODE)
    print(get_energy(TEST_STEP, copy.deepcopy(moons_test_2)))


    with open("input.txt", "r") as input_file:
        INPUT_CODE = input_file.read()
        STEP = 1000
        moons = parse_input(INPUT_CODE)
        # PART 1
        print(get_energy(STEP, copy.deepcopy(moons)))
        x_data = copy.deepcopy(moons)
        stepx = runx(x_data)

        y_data = copy.deepcopy(moons)
        stepy = runy(y_data)

        z_data = copy.deepcopy(moons)
        stepz = runz(z_data)
        print(lcm(lcm(stepx, stepy), stepz))