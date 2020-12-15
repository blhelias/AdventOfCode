"""Day 15 advent of code"""

RAW = """0,3,6"""
RAW1 = """1,3,2"""
RAW2 = """2,1,3"""
RAW3 = """1,2,3"""
RAW4 = """2,3,1"""
RAW5 = """3,2,1"""
RAW6 = """3,1,2"""

def read_input(elements_type=str):
    with open("input.txt", "r") as f:
        l = list(map(int, f.read().strip().split(",")))
    return l

if __name__=="__main__":
    X = read_input(str)
    # X = list(map(int, RAW.strip().split(",")))
    TURN1 = 2020
    TURN2 = 30000000
    print(X)
    memo = {}
    i = 1
    rep = None
    while i <= TURN2:
        last_nu = rep
        if i-1 < len(X):
            # Starting Number
            rep = X[i-1]
            memo[rep] = [i]
        else:
            if len(memo[last_nu]) < 2:
                rep = 0
            else:
                rep = memo[last_nu][-1] - memo[last_nu][-2]
            
            if rep not in memo:
                memo[rep] = [i]
            else:
                memo[rep].append(i)

        i += 1
        # print(f"Turn {i-1} : {rep} (last Nu = {last_nu}) | {memo}")

    print(rep)
