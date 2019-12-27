import copy
from typing import List, Dict, NamedTuple, Tuple
import numpy as np
from itertools import permutations

class Position:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def pot(self):
        return abs(self.x) + abs(self.y) + abs(self.z) 

    def __repr__(self):
        return "pos=<x={x}, y={y}, z={z}>".format(x=str(self.x), y=str(self.y), z=str(self.z))

class Velocity:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def kin(self):
        return abs(self.x) + abs(self.y) + abs(self.z) 

    def __repr__(self):
        return "vel=<x={x}, y={y}, z={z}>".format(x=str(self.x), y=str(self.y), z=str(self.z))

def parse_input(input_file) -> List[Position]:
    moons_pos_str = input_file.split("\n")
    return  [parse_position(moon) for moon in moons_pos_str]

def parse_position(pos_str: str) -> Position:
    pos = pos_str[1:-1].split(", ")
    return Position(int(pos[0][2:]), int(pos[1][2:]), int(pos[2][2:]))

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


def apply_velocity(pos, vel):
    """update position by applying velocity"""
    pos.x += vel.x
    pos.y += vel.y
    pos.z += vel.z
    return pos


def apply_gravity(moons, velocity) -> Tuple[List[Position], List[Velocity]]:
    
    for x in permutations(range(4), 2):
        moon1_idx = x[0] 
        moon2_idx = x[1] 
        x_vel, y_vel, z_vel = gravity(moons[moon1_idx], moons[moon2_idx])
        velocity[int(moon1_idx)].x += x_vel
        velocity[int(moon1_idx)].y += y_vel
        velocity[int(moon1_idx)].z += z_vel

    return [apply_velocity(moon, vel) for moon, vel in zip(moons, velocity)], velocity


def compute_energy(moons, velocity) -> int:
    """ pot is the abs sum of """
    sum_of_tot_energy = 0
    for moon, vel in zip(moons, velocity):

        total = moon.pot() * vel.kin()
        sum_of_tot_energy += total
    
    return sum_of_tot_energy


if __name__ == "__main__":
    TEST_CASE = """<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>"""
    TEST_STEP = 10
    moons_test = parse_input(TEST_CASE)
    velocity_test = [Velocity(0,0,0) for _ in range(4)]
    for step in range(TEST_STEP):
        moon_test, velocity_test = apply_gravity(moons_test, velocity_test)
    
    e_test = compute_energy(moon_test,velocity_test)
    
    STEP = 1000
    with open("input.txt", "r") as position_input:
        moons = parse_input(position_input.read())
        velocity = [Velocity(0,0,0) for _ in range(4)]

        for step in range(STEP):
            moons, velocity = apply_gravity(moons, velocity)
    
        e = compute_energy(moons,velocity)