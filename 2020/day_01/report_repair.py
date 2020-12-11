"""Day 1 advent of code"""

def read_input(elements_type=str):
    with open("input.txt", "r") as f:
        l = list(map(elements_type, f.read().splitlines()))
    return l

if __name__=="__main__":
    X = read_input(int)
    n = len(list(X))
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if X[i] + X[j] + X[k] == 2020:
                    print(X[i] * X[j] * X[k])
                    break
