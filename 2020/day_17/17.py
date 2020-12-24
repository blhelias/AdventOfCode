"""Day 17 advent of code"""


class GameOfLife:
    def __init__(self, grid=None, dimension=2, rounds=6, shape=5):
        self.grid = grid
        self.rounds = rounds
        self.shape = shape

    def from_string(self, s):
        if self.shapeension = 

    def from_string_3d(self, s):
        # Add padding to initial 2d grid
        x = s.split("\n")
        padd_x = (self.shape - len(x)) // 2
        padd_y = (self.shape - len(x[0])) // 2 
        x = ["." * padd_y + u + "." * padd_y for u in x]  
        padd = ["." * self.shape for _ in range(padd_x)]
        x = padd + x + padd

        empty_g = ["." * self.shape for r in range(self.shape)]
        result = []

        for i in range(self.shape): 
            if i == self.shape // 2:
                result.append(x)
            else:
                result.append(empty_g)

        self.grid = result
        return result

    def from_string_4d(self, s):
        # Add padding to initial 2d grid
        x = s.split("\n")
        padd_x = (self.shape - len(x)) // 2
        padd_y = (self.shape - len(x[0])) // 2 
        x = ["." * padd_y + u + "." * padd_y for u in x]  
        padd = ["." * self.shape for _ in range(padd_x)]
        x = padd + x + padd

        empty_g = ["." * self.shape for r in range(self.shape)]
        result = [] 
        for i in range(self.shape): 
            temp = []
            for j in range(self.shape): 
                if j == self.shape // 2 and i == self.shape // 2:
                    temp.append(x)
                else:
                    temp.append(empty_g)

            result.append(temp)

        self.grid = result
        print(result)
        print(len(result))
        print(len(result[0]))
        print(len(result[0][0]))
        print(len(result[0][0][0]))
        return result

    def run(self, cycle):
        for c in range(cycle):
            result = []
            for i in range(self.shape):
                temp = []
                for j in range(self.shape):
                    s = ""
                    for k in range(self.shape):
                        s += self.__apply_rules(i, j, k)

                    temp.append(s)
                result.append(temp)

            self.grid = result

    def __apply_rules_4d(self, x, y, z, w):
        cell = self.grid[x][y][z][w]
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
                            0 <= x_coor < len(self.grid) and \
                            0 <= y_coor < len(self.grid[0]) and \
                            0 <= z_coor < len(self.grid[0][0]) and \
                            0 <= w_coor < len(self.grid[0][0][0]) and \
                            abs(i) + abs(j) + abs(k) + abs(p) != 0
                        ):
                            if self.grid[x_coor][y_coor][z_coor][w_coor] == "#":
                                actives += 1

        if (actives == 2 or actives == 3) and cell == "#":
            next_status = "#"
        elif actives == 3 and cell == ".":
            next_status = "#"
        else:
            next_status = "."

        return next_status

    def run_4d(self, cycle):
        for c in range(cycle):
            result = []
            for i in range(self.shape):
                temp1 = []
                for j in range(self.shape):
                    temp2 = []
                    for k in range(self.shape):
                        s = ""
                        for p in range(self.shape):
                            s += self.__apply_rules_4d(i, j, k, p)

                        temp2.append(s)
                    temp1.append(temp2)
                result.append(temp1)

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

    def get_count_active_4d(self):
        actives  = 0
        for w in self.grid:
            for g in w:
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
    RAW = """.#.
..#
###"""
    SHAPE = 20
    CYCLE = 6
    with open("input.txt", "r") as f:
        X = f.read()
        # pass

    # game3d = GameOfLife(shape=SHAPE)
    # game3d.from_string_3d(RAW)
    game4d = GameOfLife(shape=SHAPE)
    # game4d.from_string_4d(RAW)
    game4d.from_string_4d(X)
    game4d.run_4d(cycle=CYCLE)
    print(game4d.get_count_active_4d())
