from collections import namedtuple
from typing import List

Point = namedtuple("Point", ["x", "y"])  # pylint: disabled
Instruction = namedtuple("Instruction", ["dir", "dist"])


def convert_instruction(instruction):
    return Instruction(instruction[0], int(instruction[1:]))


def draw_wire(instructions: List[Instruction], wire_id):
    wire = []
    coor_x = 0
    coor_y = 0
    for instruction in instructions:
        for _ in range(instruction.dist):
            if instruction.dir == "U":
                coor_y += 1

            elif instruction.dir == "D":
                coor_y -= 1

            elif instruction.dir == "R":
                coor_x += 1

            else:
                coor_x -= 1

            p = Point(coor_x, coor_y)
            wire.append(p)

    return wire


def manhattan_dist(p1: Point, p2: Point):
    """|x1 - x2| + |y1 - y2|"""
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)


def get_intersections(list1: List[Point], list2: List[Point]):
    return list(set(list1) & set(list2))


def steps(intersection: Point, points: List[Point]):
    for step, point in enumerate(points):
        if point.x == intersection.x and point.y == intersection.y:
            return step + 1


if __name__ == "__main__":
    test1 = ["R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"]
    test2 = [
        "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
        "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7",
    ]

    p0 = Point(0, 0)
    # read Input file
    with open("input.txt", "r") as input_file:
        l = []
        for wire_id, wire_instruction in enumerate(input_file):
            # YOUR CODE HERE
            wire_inst_list = wire_instruction.split(",")
            wire_instructions = [convert_instruction(i) for i in wire_inst_list]
            l.append(draw_wire(wire_instructions, wire_id))

        intersections = get_intersections(l[0], l[1])

        min_dist = float("Inf")
        min_step = float("Inf")
        for intersection in intersections:
            # compute manhattan distance for each intersections
            # and print the min one
            distance = manhattan_dist(intersection, p0)
            if distance < min_dist:
                min_dist = distance

            # get the number of steps for each intersections
            # and print the min one
            step1 = steps(intersection, l[0])
            step2 = steps(intersection, l[1])

            wire_steps = step1 + step2

            if wire_steps < min_step:
                min_step = wire_steps

        print(min_dist)
        print(min_step)

        input_file.close()
