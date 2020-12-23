"""Day 17 advent of code"""


class GameOfLife:
    def __init__(self, grid=None, rounds=6, dim=5):
        self.grid = grid
        self.rounds = rounds
        self.dim = dim

    def from_string(self, s):
        x = s.split("\n")
        empty_g = ["." * self.dim for r in range(self.dim)]
        result = []
        for i in range(self.dim): 
            if i == self.dim // 2:
                result.append(x)
            else:
                result.append(empty_g)
        self.grid = result

        print(self.grid)
        return result
    
    def run(self, cycle):
        for c in range(cycle):
            print(f"Cycle: {c}") 
            result = []
            for i in range(self.dim):
                temp = []
                for j in range(self.dim):
                    s = ""
                    for k in range(self.dim):
                        s += self.__apply_rules(i, j, k)
                    temp.append(s)
                result.append(temp)

            self.grid = result

    def __apply_rules(self, x, y, z):
        cell = self.grid[x][y][z]
        actives = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    x_coor, y_coor, z_coor = x, y, z
                    x_coor += i
                    y_coor += j
                    z_coor += k
                    if (
                        0 <= x_coor < len(self.grid) and \
                        0 <= y_coor < len(self.grid[0]) and \
                        0 <= z_coor < len(self.grid[0][0]) and \
                        abs(i) + abs(j) + abs(k) != 0
                    ):
                        if self.grid[x_coor][y_coor][z_coor] == "#":
                            actives += 1

        if (actives == 2 or actives == 3) and cell == "#":
            next_status = "#"
        elif actives == 3 and cell == ".":
            next_status = "#"
        else:
            next_status = "."

        return next_status

    def get_count_active(self):
        actives  = 0
        for g in self.grid:
            for rows in g:
                for cube in rows:
                    if cube == "#":
                        actives += 1
        return actives 

    def __repr__(self):
        g = []
        for z in range(len(self.grid)):
            g.append(f"z={z}")
            g.append("\n".join(self.grid[z]))

        repr_val  = "\n\n".join(g)

        return repr_val
                


if __name__=="__main__":
    RAW = """...............
...............
...............
...............
...............
...............
.......#.......
........#......
......###......
...............
...............
...............
...............
...............
..............."""
    DIM = 20
    CYCLE = 6
    with open("input.txt", "r") as f:
        X = f.read()

    game = GameOfLife(dim=DIM)
    # game.from_string(RAW)
    game.from_string(X)
    game.run(cycle=CYCLE)
    print(game.get_count_active())
