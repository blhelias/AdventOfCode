"""Day 14 advent of code"""
import re

RAW = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""

RAW2 = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""


def read_input(elements_type=str):
    with open("input.txt", "r") as f:
        l = list(map(elements_type, f.read().splitlines()))
    return l


def apply_mask(m, v):
    new_v = list(m)[:]
    for i in range(len(v)):
        if m[-i - 1] == "X":
            new_v[-i - 1] = v[-i - 1]
        else:
            new_v[-i - 1] = m[-i - 1]

    new_v = "".join(new_v).replace("X", "0")
    return int("".join(new_v), 2)


def decode(X):
    m = {}
    for line in X:
        if "mask" in line:
            mask = line.split("= ")[1]
        else:
            memory = re.search(r"\[([A-Za-z0-9_]+)\]", line).group(1)
            value = line.split("= ")[1]
            bin_value = bin(int(value))[2:]
            m[memory] = apply_mask(mask, bin_value)
    ans = 0

    print(sum(v for _, v in m.items()))


def find_combinations(arr):
    n = arr.count("X")
    return [format(i, "0" + str(n) + "b") for i in range(2 ** n)]


def apply_mask_v2(m, v):
    d = list(m)[:]
    for i in range(len(v)):
        if m[-i - 1] == "0":
            d[-i - 1] = v[-i - 1]
        else:
            d[-i - 1] = m[-i - 1]

    return d


def decodev2(X):
    M = {}
    C = {}
    for line in X:
        if "mask" in line:
            mask = line.split("= ")[1]
        else:
            address = re.search(r"\[([A-Za-z0-9_]+)\]", line).group(1)
            bin_address = bin(int(address))[2:]
            value = int(line.split("= ")[1])
            d = apply_mask_v2(mask, bin_address)
            idxs = [i for i in range(len(d)) if d[i] == "X"]
            nx = d.count("X")

            if nx in C:
                comb = C[nx]
            else:
                comb = find_combinations(d)
                C[nx] = comb

            for m in comb:
                arr = d[:]
                for i, c in zip(idxs, m):
                    arr[i] = c
                M[int("".join(arr), 2)] = value

    print(sum(v for _, v in M.items()))


if __name__ == "__main__":
    X = read_input(str)
    # PART1
    # X = list(map(str, RAW.splitlines()))
    decode(X)
    # PART2
    # X = list(map(str, RAW2.splitlines()))
    decodev2(X)
