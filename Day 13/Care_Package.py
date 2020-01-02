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

def put(program: str, grid: Dict[str, Tile]):
    for i in range(0, len(program), 3):
        x = program[i]
        y = program[i+1]
        tile_id = program[i+2]
        tile = Tile(x,y,tile_id)
        if x=="-1" and y=="0":
            grid["score"] = tile
        else:
            grid[tile.__hash__()] = tile
    return grid

def get_board(program) -> Dict[str, Tile]:
    return put(program, {})

def update_board(grid, program) -> Dict[str, Tile]:
    return put(program, grid)

def solve_part1(sequence):
    _, output, _, _, _ = intcode.core_intcode(sequence=sequence.split(","), 
                                              intcode_input=[1], 
                                              pos=0,
                                              relative_base_pos=0)
    intcode_soft = copy.deepcopy(output.split(","))
    grid = get_board(intcode_soft)

    return len([t for k, t in grid.items() if t.tile_id=="2" and k!="score"])

def solve_part2(sequence):
    seq_list = sequence.split(",")
    seq_list[0] = "2"
    sequence = ",".join(seq_list)
    pointer_address = 0
    relative_base = 0
    grid = None

    while True:
        dist = []
        # Test the 3 operations and see which one is the best

        # 0 (Stay on same position)
        (sequence_1, output_1, status_1,
        pointer_address_1, 
        relative_base_1) = intcode.core_intcode(sequence=copy.deepcopy(sequence.split(",")), 
                                              intcode_input=[0], 
                                              pos=copy.deepcopy(pointer_address),
                                              relative_base_pos=copy.deepcopy(relative_base))
        # -1 (left)
        (sequence_2, output_2, status_2,
        pointer_address_2, 
        relative_base_2) = intcode.core_intcode(sequence=copy.deepcopy(sequence.split(",")), 
                                              intcode_input=[-1], 
                                              pos=copy.deepcopy(pointer_address),
                                              relative_base_pos=copy.deepcopy(relative_base))

        # 1 (right)
        (sequence_3, output_3, status_3,
        pointer_address_3, 
        relative_base_3) = intcode.core_intcode(sequence=copy.deepcopy(sequence.split(",")), 
                                              intcode_input=[1], 
                                              pos=copy.deepcopy(pointer_address),
                                              relative_base_pos=copy.deepcopy(relative_base))

        grid_1, dist_1 = eval_board_state(grid, output_1.split(","))
        grid_2, dist_2 = eval_board_state(grid, output_2.split(","))
        grid_3, dist_3 = eval_board_state(grid, output_3.split(","))

        dist = [dist_1, dist_2, dist_3]
        solution_idx = dist.index(min(dist))

        if solution_idx == 0:
            sequence = sequence_1
            output = output_1
            status = status_1
            pointer_address = pointer_address_1
            relative_base = relative_base_1 
            grid = grid_1
        elif solution_idx == 1:
            sequence = sequence_2
            output = output_2
            status = status_2
            pointer_address = pointer_address_2
            relative_base = relative_base_2
            grid = grid_2
        elif solution_idx == 2:
            sequence = sequence_3
            output = output_3
            status = status_3
            pointer_address = pointer_address_3
            relative_base = relative_base_3
            grid = grid_3

        if status == 1:
            break
    
    return output

def get_ball(board):
    ball_tile = [t for k, t in board.items() if t.tile_id=="4" and k!="score"]
    return ball_tile[0]

def get_paddle(board):
    horiz_tile = [t for k, t in board.items() if t.tile_id=="3" and k!="score"]
    return horiz_tile[0]

def eval_board_state(grid, board_soft: str) -> None:
    # check where is the ball each state
    if not grid:
        grid = get_board(board_soft)
    else:
        grid = update_board(copy.deepcopy(grid), board_soft)

    ball = get_ball(grid)
    paddle = get_paddle(grid)

    return grid, abs(int(paddle.x) - int(ball.x))

if __name__ == "__main__":
    with open("input.txt", "r") as input_code:
        sequence = input_code.read()
        print(solve_part1(sequence))
        print(solve_part2(sequence))