import copy
from typing import List, Dict, NamedTuple, Tuple
import numpy as np

import sys

sys.path.append("..")
import intcode


class Point(NamedTuple):
    x: int
    y: int

    def __hash__(self):
        return str(self.x) + "," + str(self.y)


class Panel(NamedTuple):
    point: Point
    color: str

    def __hash__(self):
        return str(self.point.x) + "," + str(self.point.y)


def left_rotation(p1: Point, p2: Point):
    """use rotation matrix to compute 90 degree rotation
    p1 is the rotation center
    """
    return Point(-(p2.y - p1.y) + p2.x, p2.x - p1.x + p2.y)


def right_rotation(p1: Point, p2: Point):
    """use rotation matrix to compute 90 degree rotation
    p1 is the rotation center
    """
    return Point(-(p1.y - p2.y) + p2.x, p1.x - p2.x + p2.y)


if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        sequence = input_file.read()
        pointer_address = 0

        input_code = "0"  # PART 1
        # input_code = "1"  # PART 2

        previous_panel = None
        panel_map = {}
        relative_base = 0
        min_x = float("inf")
        max_x = float("-inf")
        min_y = float("inf")
        max_y = float("-inf")

        while True:
            (
                sequence,
                output,
                status,
                pointer_address,
                relative_base,
            ) = intcode.core_intcode(
                sequence=sequence.split(","),
                intcode_input=[input_code],
                pos=pointer_address,
                relative_base_pos=relative_base,
            )
            if status == 1:
                break

            color = output.split(",")[0]
            direction = output.split(",")[1]

            if not previous_panel:
                previous_panel = Panel(Point(0, 0), color)

                if direction == "0":
                    point = Point(-1, 0)
                else:
                    point = Point(1, 0)

                panel_map[previous_panel.__hash__()] = previous_panel
                continue
            # Turn left or right and move forward one panel
            if direction == "0":
                next_point = left_rotation(previous_panel.point, point)
            else:
                next_point = right_rotation(previous_panel.point, point)

            input_code = "0"
            if next_point.__hash__() in panel_map:
                input_code = panel_map[next_point.__hash__()].color

            panel = Panel(point, color)
            panel_map[panel.__hash__()] = panel
            previous_panel = copy.deepcopy(panel)
            point = copy.deepcopy(next_point)

            # Get shape of the map to render
            if panel.point.x > max_x:
                max_x = panel.point.x

            if panel.point.x < min_x:
                min_x = panel.point.x

            if panel.point.y > max_y:
                max_y = panel.point.y

            if panel.point.y < min_y:
                min_y = panel.point.y

        print(len(panel_map))  # PART 1 answer

        X_range = range(min_x, max_x + 1)
        Y_range = range(min_y, max_y + 1)
        grid = np.zeros((abs(min_x - max_x) + 1, abs(min_y - max_y) + 1), int)

        for x in X_range:
            for y in Y_range:
                hash_code = str(x) + "," + str(y)
                if hash_code in panel_map:
                    grid[x + abs(min_x)][y + abs(min_y)] = int(
                        panel_map[hash_code].color
                    )

        print("\n".join("".join(str(cell) for cell in row) for row in grid))  # GREJALPR
        input_file.close()
