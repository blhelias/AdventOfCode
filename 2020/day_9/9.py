"""Day 9 advent of code"""

RAWS = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""

def read_input(elements_type=str):
    with open("input.txt", "r") as f:
        l = list(map(elements_type, f.read().splitlines()))
    return l

def XMAS(arr, p):
    if len(arr) == p+1:
        item = set()
        target = arr[-1]

        for i in range(p):
            if target - arr[i] in item:
                return True
            else:
                item.add(arr[i])

        return False

    return False

def XMAS_w(arr, t):
    for i in range(len(arr)):
        if arr[i] > t:
            continue
        
        if arr[i] == t:
            return arr[i]
        
        l = []
        for j in range(i, len(arr)):
            l.append(arr[j])
            if sum(l) == t:
                return l

            elif sum(l) > t:
                continue

    return None
            

if __name__=="__main__":
    X = read_input(int)
    W = 25
    # DEBUG commands
    # X = list(map(int, RAWS.splitlines()))
    # W = 5
    for i, num in enumerate(X):
        s = X[i:i+W+1]
        if not XMAS(s, W):
            p1 = s[-1] 
            p1_idx = i + 25
            print(p1)
            break
    # PART2
    s = X[:p1_idx]
    t = p1
    rep = XMAS_w(s, t)
    print(min(rep) + max(rep))
