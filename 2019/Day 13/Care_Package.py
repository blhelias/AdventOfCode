from typing import List, Dict, NamedTuple, Tuple
import copy

import sys

sys.path.append("..")
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
        y = program[i + 1]
        tile_id = program[i + 2]
        tile = Tile(x, y, tile_id)
        if x == "-1" and y == "0":
            grid["score"] = tile
        else:
            grid[tile.__hash__()] = tile
    return grid


def get_board(program) -> Dict[str, Tile]:
    return put(program, {})


def update_board(grid, program) -> Dict[str, Tile]:
    return put(program, grid)


def solve_part1(seq):
    _, output, _, _, _ = intcode.core_intcode(
        sequence=seq.split(","), intcode_input=[], pos=0, relative_base_pos=0
    )
    intcode_soft = copy.deepcopy(output.split(","))
    grid = get_board(intcode_soft)

    return len([t for k, t in grid.items() if t.tile_id == "2" and k != "score"])


def solve_part2(sequence):
    seq = sequence.split(",")
    seq[0] = "2"
    p = 0
    r = 0
    grid = None

    s, o, status, p, r = intcode.core_intcode(
        sequence=seq, intcode_input=[], pos=p, relative_base_pos=r
    )

    while True:

        if status == 1:
            break

        grid, i = eval_board_state(grid, o.split(","))

        s, o, status, p, r = intcode.core_intcode(
            sequence=s.split(","), intcode_input=[i], pos=p, relative_base_pos=r
        )
    return o


def get_ball(board):
    ball_tile = [t for k, t in board.items() if t.tile_id == "4" and k != "score"]
    return ball_tile[0]


def get_paddle(board):
    horiz_tile = [t for k, t in board.items() if t.tile_id == "3" and k != "score"]
    return horiz_tile[0]


def eval_board_state(grid, board_soft: str) -> None:
    # check where is the ball each state
    if not grid:
        grid = get_board(board_soft)
    else:
        grid = update_board(copy.deepcopy(grid), board_soft)

    ball = get_ball(grid)
    paddle = get_paddle(grid)

    if int(ball.x) < int(paddle.x):
        i = -1
    elif int(ball.x) > int(paddle.x):
        i = 1
    else:
        i = 0

    return grid, i


if __name__ == "__main__":
    with open("input.txt", "r") as input_code:
        sequence = input_code.read()
        print(solve_part1(sequence))
        print(solve_part2(sequence))
