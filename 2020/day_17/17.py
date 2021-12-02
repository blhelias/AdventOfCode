"""Day 17 advent of code"""


class GameOfLife:
    def __init__(self, grid=None, rounds=6, shape=(5, 5, 5)):
        self.grid = grid
        self.rounds = rounds
        self.shape = tuple(x if x % 2 == 1 else x + 1 for x in shape)

    def from_string(self, s):
        # Add padding to initial 2d grid
        x = s.split("\n")

        if len(x) > self.shape[0] or len(x[0]) > self.shape[1]:
            raise ValueError(
                "Invalid Shape Input: Shape value must be greater than grid's shape"
            )

        padd_x = (self.shape[0] - len(x)) // 2
        padd_y = (self.shape[1] - len(x[0])) // 2
        x = ["." * padd_y + u + "." * padd_y for u in x]
        padd = ["." * self.shape[0] for _ in range(padd_x)]
        x = padd + x + padd
        empty_g = ["." * self.shape[1] for r in range(self.shape[0])]
        result = []
        for i in range(self.shape[3]):
            temp = []
            for j in range(self.shape[2]):
                if j == self.shape[2] // 2 and i == self.shape[3] // 2:
                    temp.append(x)
                else:
                    temp.append(empty_g)

            result.append(temp)

        self.grid = result
        return result

    def __apply_rules(self, x, y, z, w):
        cell = self.grid[w][z][x][y]
        actives = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    for p in range(-1, 2):
                        x_coor, y_coor, z_coor, w_coor = x, y, z, w
                        x_coor += i
                        y_coor += j
                        z_coor += k
                        w_coor += p
                        if (
                            0 <= x_coor < len(self.grid[0][0])
                            and 0 <= y_coor < len(self.grid[0][0][0])
                            and 0 <= z_coor < len(self.grid[0])
                            and 0 <= w_coor < len(self.grid)
                            and abs(i) + abs(j) + abs(k) + abs(p) != 0
                        ):
                            if self.grid[w_coor][z_coor][x_coor][y_coor] == "#":
                                actives += 1
        if (actives == 2 or actives == 3) and cell == "#":
            next_status = "#"
        elif actives == 3 and cell == ".":
            next_status = "#"
        else:
            next_status = "."

        return next_status

    def run(self, cycle):
        for c in range(cycle):
            result = []
            for w in range(self.shape[3]):
                temp1 = []
                for z in range(self.shape[2]):
                    temp2 = []
                    for x in range(self.shape[0]):
                        s = ""
                        for y in range(self.shape[1]):
                            s += self.__apply_rules(x, y, z, w)

                        temp2.append(s)
                    temp1.append(temp2)
                result.append(temp1)

            self.grid = result

    def get_count_active(self):
        actives = 0
        for w in range(self.shape[3]):
            for z in range(self.shape[2]):
                for x in range(self.shape[0]):
                    for y in range(self.shape[1]):
                        if self.grid[w][z][x][y] == "#":
                            actives += 1

        return actives

    def __repr__(self):
        g = []
        for w in range(len(self.grid)):
            for z in range(len(self.grid[0])):
                g.append(f"z={z} | w={w}")
                g.append("\n".join(self.grid[w][z]))

        repr_val = "\n\n".join(g)

        return repr_val


if __name__ == "__main__":
    RAW = """.#.
..#
###"""
    SHAPE_P1 = (21, 21, 21, 1)
    SHAPE_P2 = (21, 21, 21, 21)
    CYCLE = 6
    with open("input.txt", "r") as f:
        X = f.read()

    game_p1 = GameOfLife(shape=SHAPE_P1)
    game_p1.from_string(X)
    game_p1.run(cycle=CYCLE)
    print(game_p1.get_count_active())

    game_p2 = GameOfLife(shape=SHAPE_P2)
    game_p2.from_string(X)
    game_p2.run(cycle=CYCLE)
    print(game_p2.get_count_active())
