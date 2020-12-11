"""Day 14 advent of code"""

def read_input(elements_type=str):
    with open("input.txt", "r") as f:
        l = list(map(elements_type, f.read().splitlines()))
    return l

if __name__=="__main__":
    X = read_input(str)
    print(X)
