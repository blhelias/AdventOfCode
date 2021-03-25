"""Day 3 advent of code"""


def parse(s):
    top, bottom = s.split("\n\n")
    top = top.strip().split("\n")
    bottom = bottom.strip().split("\n")

    rules = {}
    for rule in top:
        r = rule.split(": ")

        rules[r[0]] = [tuple(x.split(" ")) for x in r[1].split(" | ")]

    return rules, bottom


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        s = f.read()

    t, b = parse(s)
    print(t)
