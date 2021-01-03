"""
Day 18 advent of code
Code provenant de programmation efficace
Christoph Durr Jill Jênn Vie
"""

def parse_input(s):
    x = s.split("\n")
    return x


def expr_eval(cell, expr):

    if isinstance(expr, tuple):
        (left, op, right) = expr
        l = expr_eval(cell, left)
        r = expr_eval(cell, right)

        if op == "+":
            return l + r

        if op == "*":
            return l * r

    elif isinstance(expr, int):
        return expr

    else:
        cell[exp] = expr_eval(cell, cell[expr])
        return cell[expr]

def expr_parse(line, priority):
    # on procède avec 2 piles, une pour les opérateurs une pour les valeurs.
    vals = []
    ops = []
    for tok in line + [";"]:

        if tok in priority: # ça veut dire que tok est un opérateur

            while tok != "(" and ops and priority[ops[-1]] >= priority[tok]:
                right = vals.pop()
                left = vals.pop()
                vals.append((left, ops.pop(), right))

            if tok == ")":
                ops.pop()
            else:
                ops.append(tok)

        elif tok.isdigit():
             vals.append(int(tok))
        else:
            vals.append(tok)
    
    return vals.pop()

def run(raw, priority):
    p1 = expr_parse(list(raw.replace(" ", "")), priority)
    return expr_eval({}, p1)    


if __name__=="__main__":
    PRIORITY1 = {";": 0, "(": 1, ")": 2, "+": 3, "*": 3}  
    PRIORITY2 = {";": 0, "(": 1, ")": 2, "+": 4, "*": 3}  
    #
    # TESTS
    #
    RAW1 = "2 * 3 + (4 * 5)"
    RAW2 = "5 + (8 * 3 + 9 + 3 * 4 * 3)"
    RAW3 = "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"
    RAW4 = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"
    # PART1
    assert run(RAW1, PRIORITY1) == 26
    assert run(RAW2, PRIORITY1) == 437
    assert run(RAW3, PRIORITY1) == 12240
    assert run(RAW4, PRIORITY1) == 13632
    # PART2
    assert run(RAW1, PRIORITY2) == 46
    assert run(RAW2, PRIORITY2) == 1445
    assert run(RAW3, PRIORITY2) == 669060
    assert run(RAW4, PRIORITY2) == 23340

    #
    # PUZZLE
    #
    with open("input.txt") as f:
        X = f.read()

    lines = parse_input(X)
    print(sum(run(line, PRIORITY1) for line in lines if line))
    print(sum(run(line, PRIORITY2) for line in lines if line))
