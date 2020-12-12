"""Day 12 advent of code"""
import math

from collections import namedtuple
from typing import NamedTuple
from math import sin, cos, radians, pi, atan2, degrees

RAWS = """F10
N3
F7
R90
F11
L180"""

class Instruction(NamedTuple):
    action: str
    value: int

    @staticmethod
    def from_string(r):
        return Instruction(r[0], int(r[1:]))

def read_input(elements_type=str):
    with open("input.txt", "r") as f:
        l = list(map(elements_type, f.read().splitlines()))
    return l

def rotate(point, angle):

    ox, oy = (0, 0)
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return [round(qx, 0), round(qy, 0)]

def move_ship_wp1(x, y, wp, instruction):
    action, value = instruction
    directions = {"N": (0, +1), "S": (0, -1), "E": (+1, 0), "W": (-1, 0)}
    if action == "F":
        x += value * wp[0]
        y += value * wp[1]
    elif action == "R":
        wp = rotate(wp, -radians(value))
    elif action == "L":
        wp = rotate(wp, radians(value))
    else:
        x += value * directions[action][0]
        y += value * directions[action][1]

    return x, y, wp

def solve1(X, way_point):
    x = 0
    y = 0
    
    for instruction in X:
        x, y, way_point = move_ship_wp1(x, y, way_point, instruction)
    return x, y

def move_ship_wp2(x, y, wp, instruction):
    action, value = instruction
    directions = {"N": (0, +1), "S": (0, -1), "E": (+1, 0), "W": (-1, 0)}
    if action == "F":
        x += value * wp[0]
        y += value * wp[1]
    elif action == "R":
        wp = rotate(wp, -radians(value))
    elif action == "L":
        wp = rotate(wp, radians(value))
    else:
        wp[0] += value * directions[action][0]
        wp[1] += value * directions[action][1]

    return x, y, wp

def solve2(X, way_point):
    x = 0
    y = 0
    
    for instruction in X:
        x, y, way_point = move_ship_wp2(x, y, way_point, instruction)

    return x, y


if __name__=="__main__":
    X = read_input(str)
    # X = list(map(str, RAWS.splitlines()))
    X = [Instruction.from_string(x) for x in X]

    # PART 1
    wp1 = [+1, 0]
    x1, y1 = solve1(X, wp1)
    print(abs(x1) + abs(y1))

    # PART 2
    wp2 = [+10, +1]
    x2, y2 = solve2(X, wp2)
    print(abs(x2) + abs(y2))
