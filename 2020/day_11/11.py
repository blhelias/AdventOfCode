"""Day 11 advent of code"""
RAWS = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

delta_x = [[-1, 0, 1], [-1, 1], [-1, 0, 1]]
delta_y = [[-1, -1, -1], [0, 0], [1, 1, 1]]


def read_input(elements_type=str):
    with open("input.txt", "r") as f:
        l = [list(x) for x in list(map(elements_type, f.read().splitlines()))]
    return l


def scan_adjacent(grid, i, j):
    """This function scans all adjacents seats around a given seat"""
    counter = {"#": 0, "L": 0, ".": 0}
    for lx, ly in zip(delta_x, delta_y):
        for dx, dy in zip(lx, ly):
            x = i + dx
            y = j + dy
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                counter[grid[x][y]] += 1

    return counter["#"], counter["L"]


def draw_seat_map1(grid):
    h = len(grid)
    w = len(grid[0])
    stabilized = True
    new_grid = [row[:] for row in grid]

    for i in range(h):
        for j in range(w):
            occ, emp = scan_adjacent(grid, i, j)
            # print(grid[i][j], occ, emp, floor)
            if grid[i][j] == "L" and occ == 0:
                new_grid[i][j] = "#"
                stabilized = False
            elif grid[i][j] == "#" and occ >= 4:
                new_grid[i][j] = "L"
                stabilized = False

    return new_grid, stabilized


def scan_first(grid, i, j):
    """This function scans all adjacents seats around a given seat"""
    counter = {"#": 0, "L": 0}

    for lx, ly in zip(delta_x, delta_y):
        for dx, dy in zip(lx, ly):
            x = i
            y = j
            found_seat = False
            while not found_seat:
                x += dx
                y += dy
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                    occupied = False
                    if grid[x][y] == "L":
                        counter[grid[x][y]] += 1
                        found_seat = True
                    elif grid[x][y] == "#":
                        counter[grid[x][y]] += 1
                        found_seat = True
                else:
                    found_seat = True

    return counter["#"], counter["L"]


def draw_seat_map2(grid):
    h = len(grid)
    w = len(grid[0])
    stabilized = True
    new_grid = [row[:] for row in grid]

    for i in range(h):
        for j in range(w):
            occ, emp = scan_first(grid, i, j)
            if grid[i][j] == "L" and occ == 0:
                new_grid[i][j] = "#"
                stabilized = False
            elif grid[i][j] == "#" and occ >= 5:
                new_grid[i][j] = "L"
                stabilized = False

    return new_grid, stabilized


def count_occ(grid):
    c = 0
    for row in grid:
        for seat in row:
            if seat == "#":
                c += 1
    return c


if __name__ == "__main__":
    X = read_input(str)
    # X = [list(x) for x in list(map(str, RAWS.splitlines()))]
    stabilized = False
    while not stabilized:
        X, stabilized = draw_seat_map1(X)

    print(count_occ(X))

    # PART 2
    X = read_input(str)
    # X = [list(x) for x in list(map(str, RAWS.splitlines()))]
    stabilized = False
    while not stabilized:
        X, stabilized = draw_seat_map2(X)

    print(count_occ(X))
