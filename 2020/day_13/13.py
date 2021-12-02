"""Day 13 advent of code"""


def read_input(elements_type=str):
    with open("input.txt", "r") as f:
        l = list(map(elements_type, f.read().splitlines()))
    return l


RAW = """939
7,13,x,x,59,x,31,19"""


def earliest_bus(X):
    start = int(X[0])
    found = False
    while not found:
        for bid in X[1].split(","):
            if bid.isdigit() and int(start) % int(bid) == 0:
                found = True
                print((start - int(X[0])) * int(bid))
                break
        start += 1


def match_list(x):
    ids = []
    for idx, v in enumerate(x):
        if v != "x":
            k = int(v)
            i = idx + 1
            i %= k
            ids.append((k - (i % k), k))


# n busses
# bus k at index i departs at a time t+i
# t+i % k == 0
# t % k == -i
# t % k = k-i
# index = (k - (i%k)) % k
def get_earliest_time(data):
    ids = []
    fullProduct = 1
    data = data.split(",")
    for i in range(len(data)):
        item = data[i]
        if item != "x":
            k = int(item)
            i = i % k
            ids.append(((k - i) % k, k))
            fullProduct *= k

    total = 0
    for i, k in ids:
        partialProduct = fullProduct // k

        inverse = mod_inverse(partialProduct, k)
        assert (inverse * partialProduct) % k == 1

        term = inverse * partialProduct * i
        total += term

    return total % fullProduct


def mod_inverse(a, n):
    # find some x such that (a*x) % n == 1
    a = a % n
    if n == 1:
        return 1
    for x in range(1, n):
        if (a * x) % n == 1:
            return x


if __name__ == "__main__":

    # PART 1
    X = read_input(str)
    # X = list(map(str, RAW.splitlines()))
    earliest_bus(X)

    # Part 2

    #
    # UNIT TESTS
    #
    # assert match_list("17,x,13,19") == 3417
    # assert match_list("67,7,59,61") == 754018
    # assert match_list("67,x,7,59,61") == 779210
    # assert match_list("67,7,x,59,61") == 1261476
    # assert match_list("1789,37,47,1889") == 1202161486

    # X = list(map(str, RAW.splitlines()))
    # match_list(X[1].split(","))
    # part two
    X = read_input(str)
    print(get_earliest_time(X[1]))
