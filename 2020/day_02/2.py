"""Day 2 advent of code"""


def read_input(elements_type=str):
    with open("input.txt", "r") as f:
        l = list(map(elements_type, f.read().splitlines()))
    return l


if __name__ == "__main__":
    X = read_input(str)
    C1 = 0
    C2 = 0
    for line in X:
        x = line.split(" ")
        o = list(map(int, (x[0].split("-"))))
        p = x[2]
        l = x[1].split(":")[0]

        ## PART1
        count = 0
        for i in p:
            if i == l:
                count += 1

        if count <= o[1] and count >= o[0]:
            C1 += 1

        ## PART2
        if p[o[0] - 1] == l and p[o[1] - 1] != l:
            C2 += 1
        if p[o[0] - 1] != l and p[o[1] - 1] == l:
            C2 += 1

    print(C1)
    print(C2)
