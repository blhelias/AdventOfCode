"""Day 18 advent of code"""


def parse_input(s):
    x = s.split("\n")
    return x

def parse(expr):
    def _helper(iter):
        items = []
        for item in iter:
            if item == '(':
                result, closeparen = _helper(iter)
                if not closeparen:
                    raise ValueError("bad expression -- unbalanced parentheses")
                items.append(result)
            elif item == ')':
                return items, True
            else:
                items.append(item)
        return items, False

    return _helper(iter(expr))[0]


def compute(expr):
    ans = 0
    for i in range(len(expr)):

        if expr[i] in ["+", "*"]:
            left = expr[i-1]
            right = expr[i+1]

            if isinstance(left, list):
                left = compute(left)
            if isinstance(right, list):
                right = compute(right)

            left = int(left)
            right = int(right)
            if expr[i] == "+":
                if ans == 0:
                    ans = left + right
                else:
                    ans += right
            elif expr[i] == "*":
                if ans == 0:
                    ans = left * right
                else:
                    ans *= right

    return ans

def evaluate(line):
    x = parse_input(line)
    p = parse(x[0].replace(" ",""))
    res = compute(p)
    return res

if __name__=="__main__":
    #
    # TESTS
    #
    RAW1 = "2 * 3 + (4 * 5)"
    RAW2 = "5 + (8 * 3 + 9 + 3 * 4 * 3)"
    RAW3 = "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"
    RAW4 = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"

    assert evaluate(RAW1) == 26
    assert evaluate(RAW2) == 437
    assert evaluate(RAW3) == 12240
    assert evaluate(RAW4) == 13632

    #
    # PUZZLE
    #
    with open("input.txt") as f:
        X = f.read()

    lines = parse_input(X)
    print(sum(evaluate(line) for line in lines))
