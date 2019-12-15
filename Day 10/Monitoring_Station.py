from collections import namedtuple
from typing import List, NamedTuple

class Point(NamedTuple):
    x: int
    y: int

    def __hash__(self):
        return str(x)+str(y)


def is_colinear(p1: Point, p2:Point, p3:Point) -> bool:
    a = p1.x * (p2.y - p3.y) + p2.x * (p3.y - p1.y) + p3.x * (p1.y - p2.y) 
    if a == 0:
        return True
    return False


def parse_map(map: str) -> List[List[Point]]:
    map_list = map.split("\n")
    asteroids_map = [list(x) for x in map_list]
    return asteroids_map


def plot_line_low(p0: Point, p1: Point):
    line = []
    dx = p1.x - p0.x
    dy = p1.y - p0.y
    yi = 1

    if dy < 0:
        yi = -1
        dy = -dy

    D = 2*dy - dx
    y = p0.y

    for x in range(p0.x, p1.x+1):
        line.append(Point(x, y))

        if D > 0:
            y = y + yi
            D = D - 2*dx

        D = D + 2*dy

    line = clean_line(line)

    return line


def plot_line_high(p0: Point, p1: Point):
    line = []
    dx = p1.x - p0.x
    dy = p1.y - p0.y
    xi = 1
    if dx < 0:
        xi = -1
        dx = -dx
    
    D = 2*dx - dy
    x = p0.x

    for y in range(p0.y, p1.y+1):
        line.append(Point(x, y))

        if D > 0:
            x = x + xi
            D = D - 2*dy

        D = D + 2*dx
        
    line = clean_line(line)
    return line


def plot_line_xequal(p0: Point, p1: Point):
    line = []
    direction = 1

    if p1.y-p0.y < 0:
        direction = -1

    for i in range(abs(p0.y-p1.y)+1):
        line.append(Point(p0.x, p0.y+(i)*direction))

    return line


def plot_line_yequal(p0: Point, p1: Point):
    line = []
    direction = 1

    if p1.x-p0.x < 0:
        direction = -1

    for i in range(abs(p0.x-p1.x)+1):
        line.append(Point(p0.x + i*direction, p0.y))
    
    return line


def clean_line(line):
    clean_line = []
    for i in range(1, len(line)-1):
        if is_colinear(line[0], line[i], line[-1]):
            clean_line.append(line[i])
    
    clean_line = [line[0]] + clean_line + [line[-1]]

    return clean_line 


def plot_line(p0: Point, p1: Point):
    if (p1.y - p0.y) == 0:
        full_line = plot_line_yequal(Point(p0.x, p0.y), 
                                     Point(p1.x, p1.y))

    elif (p1.x - p0.x) == 0:
        full_line = plot_line_xequal(Point(p0.x, p0.y), 
                                     Point(p1.x, p1.y))

    elif abs(p1.y - p0.y) < abs(p1.x - p0.x):
        if p0.x > p1.x:
            full_line = plot_line_low(Point(p1.x, p1.y), 
                                      Point(p0.x, p0.y))
        else:
            full_line = plot_line_low(Point(p0.x, p0.y), 
                                      Point(p1.x, p1.y))
    
    else:
        if p0.y > p1.y:
            full_line = plot_line_high(Point(p1.x, p1.y), 
                                       Point(p0.x, p0.y))
        else:
            full_line = plot_line_high(Point(p0.x, p0.y), 
                                       Point(p1.x, p1.y))

    if full_line[0] != p0:
        full_line.reverse()

    return full_line


def find_best_spot(map: str) -> str:
    max_asteroids = 0
    asteroids_map = parse_map(map)

    for x_centroid in range(len(asteroids_map)):

        for y_centroid in range(len(asteroids_map[x_centroid])):

            if asteroids_map[x_centroid][y_centroid] == ".":
                continue

            centroid = Point(x_centroid, y_centroid)

            l = []

            for pos_x in range(len(asteroids_map)):
                for pos_y in range(len(asteroids_map[pos_x])):

                    if asteroids_map[pos_x][pos_y] == ".":
                        continue

                    point = Point(pos_x, pos_y)
                    
                    if point == centroid:
                        continue
 
                    l.append(plot_line(centroid, point))

            reponse = []
            for x in range(len(l)):
                counter = 0
                for y in range(len(l[x])):

                    if l[x][y] in reponse:
                        counter += 1

                    if asteroids_map[l[x][y].x][l[x][y].y] == "#" and counter < 1 and l[x][y] != centroid:

                        reponse.append(l[x][y])
                        counter += 1
            
            if len(reponse) > max_asteroids:
                max_asteroids = len(reponse)
                best_location = centroid

    return max_asteroids, best_location

if __name__ =="__main__":
    # Itérer sur chaque centroid
    p_1 = Point(0, 0)
    p_0 = Point(0, 4)
    p_2 = Point(2, 0)
    # print(plot_line(p_0, p_1))
    # print(plot_line(p_2, p_1))
    # print()
    test1 = """.#..#
.....
#####
....#
...##"""

    test2 = """....#
.....
.....
.....
#...."""

    test3 = """....#
....#
.....
....#
....."""

    test4 = """.#...
.....
.#...
.....
....."""

    test5 = """....#
.....
.....
.....
...#."""


    test6 = """......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####"""

    test7 = """#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###."""

    test8 = """.#..#..###
####.###.#
....###.#.
..###.##.#
##.##.#.#.
....###..#
..#.#..#.#
#..#.#.###
.##...##.#
.....#.#.."""

    test9 = """.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##"""

    print(find_best_spot(test1))
    print(find_best_spot(test6))
    print(find_best_spot(test7))
    print(find_best_spot(test8))
    print(find_best_spot(test9))

    with open("input.txt", "r") as input_puzzle:
        map_ast = input_puzzle.read()
        print(find_best_spot(map_ast))
