"""Day 8 advent of code"""
import copy
from collections import namedtuple
from typing import NamedTuple


class Instruction(NamedTuple):
    op: str
    arg: int
        

class BootCode:
    def __init__(self, instructions):
        self.instructions = instructions
        self.acc = 0
        self.visited = []
    
    @classmethod
    def from_string(cls, raws):
        instructions = [Instruction(inst.split(" ")[0], int(inst.split(" ")[1])) \
                for inst in raws]
        return cls(instructions)

    def run(self, debug=None):

        infinite_loop = False
        i = 0

        while not infinite_loop and i < len(self.instructions):

            if i not in self.visited:
                self.visited.append(i)
                inst = self.instructions[i]

                if debug and i == debug:
                    if inst.op == "jmp":
                        inst = Instruction("nop", inst.arg)
                    elif inst.op == "nop":
                        inst = Instruction("jmp", inst.arg)

                if inst.op == "nop":
                    i += 1

                elif inst.op == "jmp":
                    i += inst.arg
                    
                elif inst.op == "acc":
                    self.acc += inst.arg
                    i += 1
            
            else:
                infinite_loop = True
                return False

        return True

    def reset(self):
        self.acc = 0
        self.visited = []


def read_input(elements_type=str):
    with open("input.txt", "r") as f:
        l = list(map(elements_type, f.read().splitlines()))
    return l


if __name__=="__main__":
    X = read_input(str)
    bc = BootCode.from_string(X)

    # Part 1
    bc.run()
    print(bc.acc)

    # Part 2
    for i in range(max(bc.visited), 0, -1):
        bc.reset()
        if bc.run(debug=i):
            print(bc.acc)
            break
