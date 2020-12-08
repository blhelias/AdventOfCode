"""Day 8 advent of code"""
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
        i = 0
        while i < len(self.instructions):

            if i not in self.visited:
                self.visited.append(i)
                inst = self.instructions[i]

                if inst.op == "nop":
                    i += 1
                elif inst.op == "jmp":
                    i += inst.arg
                elif inst.op == "acc":
                    self.acc += inst.arg
                    i += 1
            
            else:
                return False

        return True

    def reset(self):
        self.acc = 0
        self.visited = []
    

def swap_nop_jmp(lines, idx):
    clone = lines[:]

    if "jmp" in clone[idx]:
        clone[idx] = clone[idx].replace("jmp", "nop")
    elif "nop" in clone[idx]:
        clone[idx] = clone[idx].replace("nop", "jmp")
    else:
        return None

    return clone

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
        instructions = swap_nop_jmp(X, i)
        if instructions:
            bc_debug = BootCode.from_string(instructions)
            has_ended = bc_debug.run()
            if has_ended:
                print(bc_debug.acc)
                break
