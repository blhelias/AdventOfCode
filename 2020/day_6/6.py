"""Day 6 advent of code"""

def read_input(elements_type=str):
    with open("input.txt", "r") as f:
        l = list(map(elements_type, f.read().split("\n\n")))
    return l

if __name__=="__main__":
    X = read_input(str)

    # PART 1
    print(sum([len(set([a for a in x if a and a != '\n'])) for x in X]))

    # PART 2
    p2 = []
    for x in X:
        y_ans = x.split("\n")
        y_ans = [ x for x in y_ans if x is not '' ]
        p = [set(y_ans) for y_ans in y_ans]
        u = set.intersection(*p)
        p2.append(len(u))

    print(sum(p2))
