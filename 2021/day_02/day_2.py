from typing import NamedTuple
from collections import namedtuple

class Instruction(NamedTuple):
    """a docstring"""
    cmd: str
    dist: int

def main1(input_file):
    input_str = input_file.split("\n")
    horizontal = 0
    depth = 0
    Inst = namedtuple("Instruction", "cmd dist")
    for i in range(len(input_str)):
        inst = Inst(input_str[i].split(" ")[0], int(input_str[i].split(" ")[1]))
        if inst.cmd == "forward":
            horizontal += inst.dist
        elif inst.cmd == "up":
            depth -= inst.dist
        elif inst.cmd == "down":
            depth += inst.dist
    
    print(horizontal * depth)

def main2(input_file):
    input_str = input_file.split("\n")
    horizontal = 0
    depth = 0
    aim = 0
    Inst = namedtuple("Instruction", "cmd dist")
    for i in range(len(input_str)):
        inst = Inst(input_str[i].split(" ")[0], int(input_str[i].split(" ")[1]))
        if inst.cmd == "forward":
            horizontal += inst.dist
            depth += aim * inst.dist
        elif inst.cmd == "up":
            aim -= inst.dist
        elif inst.cmd == "down":
            aim += inst.dist
        
    print(horizontal * depth)



if __name__ == "__main__":
    # Test our functions
    TEST = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""
    # Read input file
    main1(TEST)
    main2(TEST)
    with open("input.txt", "r") as input_file:
        main1(input_file.read())
        main2(input_file.read())

    input_file.close()