"""
- First, it will output a value indicating the color to paint the panel the robot is over: 0 means to paint the panel black, and 1 means to paint the panel white.
- Second, it will output a value indicating the direction the robot should turn: 0 means it should turn left 90 degrees, and 1 means it should turn right 90 degrees.

"""
import logging
import copy
from typing import List, Dict, NamedTuple, Tuple
from itertools import permutations
from collections import namedtuple
import numpy as np

import sys 
sys.path.append('..')
import intcode

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
# création d'un second handler qui va rediriger chaque écriture de log
# sur la console
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
logger.addHandler(stream_handler)


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
    return Point(-(p2.y-p1.y)+p2.x, p2.x-p1.x+p2.y)

def right_rotation(p1: Point, p2: Point): 
    return Point(-(p1.y-p2.y)+p2.x, p1.x-p2.x+p2.y)

if __name__ == "__main__":
    with open("input.txt", 'r') as input_file:
        sequence = input_file.read()
        running = True
        pointer_address = 0
        input_code_part1 = "0"
        input_code_part2 = "1"
        previous_panel = None
        panel_map = {}
        relative_base = 0

        while running:
            sequence, output, status, pointer_address, relative_base = intcode.core_intcode(sequence=sequence.split(","), 
                                                                                            intcode_input=[input_code], 
                                                                                            pos=pointer_address,
                                                                                            relative_base_pos=relative_base)
            if status == 1:
                running = False

            color = output.split(",")[0]
            direction = output.split(",")[1]
            
            if not previous_panel:
                previous_panel = Panel(Point(0,0), color)
                if direction == "0":
                    point = Point(-1, 0)
                else:
                    point = Point(1, 0)

                panel_map[previous_panel.__hash__()] = previous_panel
                input_code = "0"
                continue
            
            # Turn left or right according to the previous segment
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

        logger.info(len(panel_map))
 
        min_x = float("inf")
        max_x = float("-inf")
        min_y = float("inf")
        max_y = float("-inf")
        for _, panel in panel_map.items():
            if panel.point.x > max_x:
                max_x = panel.point.x
            elif panel.point.x < min_x:
                min_x = panel.point.x
            elif panel.point.y > max_y:
                max_y = panel.point.y
            elif panel.point.y < min_y:
                min_y = panel.point.y
        
        # logger.info("max X: "+ str(max_x))
        # logger.info("min X: "+ str(min_x))
        # logger.info("max Y: "+ str(max_y))
        # logger.info("min Y: "+ str(min_y))
        X_range = range(-50, 45)
        Y_range = range(-35, 35) 
        grid = np.zeros((95, 70), int)

        for x in X_range:
            for y in Y_range:
                hash_code = str(x) + "," + str(y)
                if hash_code in panel_map:
                    grid[x+50][y+35] = int(panel_map[hash_code].color)
        
        logger.info('\n'.join(''.join(str(cell) for cell in row) for row in grid)) # GREJALPR