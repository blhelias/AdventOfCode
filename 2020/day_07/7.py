"""Day 7 advent of code"""

INPUT_SAMPLE_1 = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

INPUT_SAMPLE_2 = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""

def read_input(test_string=None, elements_type=str):
    if test_string:
        return list(map(elements_type, test_string.splitlines()))

    with open("input.txt", "r") as f:
        l = list(map(elements_type, f.read().splitlines()))
    return l


def build_graph(rules):
    g = {}
    for r in rules:
        if r[0] not in g:
            g[r[0]] = [(r[1], r[2])]
        else:
            g[r[0]] = g[r[0]] + [(r[1], r[2])]

    return g

def transpose(rules):
    return [(r[1], r[0], r[2]) for r in rules]

def search1(g, start):
    q = g[start]
    vis = [start[0]]
    c = 0
    while len(q) != 0:
        cur = q.pop(0)
        if cur[0] not in vis:
            vis.append(cur[0])
            c += 1

            if cur[0] in g:
                q += [x for x in g[cur[0]] if x[0] not in vis]

    return c


def dfs(graph, node):
    
    if node[0] not in graph:
        return 1

    total = 0
    for child in graph[node[0]]:
        total += child[1] * dfs(graph, child)

    if node[0] == "shiny gold":
        return total

    return total + 1  
            

if __name__=="__main__":
    # rules = read_input(test_string=INPUT_SAMPLE_1, elements_type=str)
    # rules = read_input(test_string=INPUT_SAMPLE_2, elements_type=str)
    rules = read_input(elements_type=str)
    X = []
    for rule in rules:
        rule = rule.split(" contain ")
        parent = rule[0].split(" bags")[0]
        children = rule[1].split(", ")

        for b in children:
            if b != "no other bags.":
                b = b.split(" bag")[0]
                quantity = b.split(" ")[0]
                child = b.split(quantity + " ")[1] 
                X.append((parent, child, int(quantity)))
                
    G1 = build_graph(transpose(X))
    start = "shiny gold"
    # PART 1
    rep = search1(G1, start)
    print(rep)
    # PARRT 2
    G2 = build_graph(X)
    print(dfs(G2, (start, 0)))
