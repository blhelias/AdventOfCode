"""Day 10 advent of code"""

RAWS1 = """16
10
15
5
1
11
7
19
6
12
4"""


RAWS2 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""

def solve1(X):
    X = [0] + X
    X.sort()
    score = {1: 0, 3: 1}
    for i in range(len(X) - 1):
        sub = X[i + 1] - X[i]
        if sub in score:
            score[sub] += 1

    return score[1] * score[3]

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

@memoize
def dp(i):
    if i == len(X) - 1:
        return 1
    ans = 0
    for j in range(i+1, len(X)):
        if X[j] - X[i] <= 3:
            ans += dp(j)
    return  ans

def read_input(elements_type=str):
    with open("input.txt", "r") as f:
        l = list(map(elements_type, f.read().splitlines()))
    return l

if __name__=="__main__":
    # PArt 1
    X1 = list(map(int, RAWS1.splitlines()))
    X2 = list(map(int, RAWS2.splitlines()))
    X3 = read_input(int)
    assert solve1(X1) == 35
    assert solve1(X2) == 220
    print(solve1(X3))
    # PArt 2
    X = read_input(int)
    X = [0] + X + [max(X) + 3]
    X.sort()
    print(dp(0))
