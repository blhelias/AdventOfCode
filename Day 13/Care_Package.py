from typing import List, Dict, NamedTuple, Tuple
import copy
import sys 
sys.path.append('..')
import intcode

class Tile(NamedTuple):
    x: int
    y: int
    tile_id: int

    def __hash__(self):
        return str(self.x) + "," + str(self.y)

def solve_part1(sequence):
    _, output, _, _, _ = intcode.core_intcode(sequence=sequence.split(","), 
                                              intcode_input=[None], 
                                              pos=0,
                                              relative_base_pos=0)
    intcode_soft = copy.deepcopy(output.split(","))
    grid = {}

    for i in range(0, len(intcode_soft), 3):
        tile = Tile(intcode_soft[i], intcode_soft[i+1], intcode_soft[i+2])
        grid[tile.__hash__()] = tile

    return len([t for k, t in grid.items() if t.tile_id=="2"])

def solve_part2(sequence):
    sequence_list = sequence.split(",")
    sequence_list[0] = "2"
    sequence, output, status, pointer_address, relative_base = intcode.core_intcode(sequence=sequence.split(","), 
                                                                                    intcode_input=[None], 
                                                                                    pos=0,
                                                                                    relative_base_pos=0)
    return output

if __name__ == "__main__":
    with open("input.txt", "r") as input_code:
        sequence = input_code.read()
        print(solve_part1(sequence))
        print(solve_part2(sequence))