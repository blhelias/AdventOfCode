"""Day 3 advent of code"""
from functools import reduce

def read_input(t=str):
    with open("input.txt", "r") as f:
        l = [list(i) for i in f.read().splitlines()]
    return l

def get_trees_n(X, s):
    x = 0
    y = 0
    p = 1 if X[x][y] == "#" else 0
    shape = (len(X), len(X[0]))

    while x <= shape[0]-1:
        x += s[0]
        y += s[1]

        if y > shape[1]-1:
            y = y - shape[1]

        if X[x][y] == "#":
            p += 1
    return p

def main():
    X = read_input(str)
    slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    rep = [get_trees_n(X, s) for s in slopes] 
    print(reduce(lambda x, y: x*y, rep))


if __name__=="__main__":
    main()
