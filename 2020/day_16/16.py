"""Day 16 advent of code"""

from typing import NamedTuple, List
from collections import namedtuple

# 
# DATACLASS
#
class Rule(NamedTuple):
    # name: str
    range1: List[int]
    range2: List[int]

    @staticmethod
    def from_string(raws):
        # name = raws.split(": ")[0]
        r = raws.split(": ")[1]
        left = r.split("or ")[0]
        right = r.split("or ")[1]
        rule = Rule(
            # name, 
            [int(left.split("-")[0]),  int(left.split("-")[1])],
            [int(right.split("-")[0]),  int(right.split("-")[1])]
        )
        return rule

class Note(NamedTuple):
    rules: List[Rule]
    ticket: List[str]
    nearby_ticket: List[str]

def parse(s):
    rule, t, nearby_t = [], [], []
    seen = []
    for line in s.split("\n"):
        if "your ticket:" == line:
            seen.append("s2")
        elif "nearby tickets:" == line:
            seen.append("s3")
        else:
            if len(line) > 4:
                if not seen:
                    rule.append(Rule.from_string(line))
                elif len(seen) == 1:
                    t.append(line)
                else:
                    nearby_t.append(line)

    return Note(rule, t, nearby_t)

def get_invalid_tickets(rules, fields):
    fields = list(map(int, fields.split(",")))
    rep1 = []
    for f in fields:
        rep2 = []
        for r1, r2 in rules:
            if r1[0]<=f<=r1[1] or r2[0]<=f<=r2[1]:
                rep2.append(True)
            else:
                rep2.append(False)

        rep1.append(rep2)

    i_fields = [any(x) for x in rep1]

    for i in range(len(i_fields)):
        if not i_fields[i]:
            return fields[i]
    
    return None

def get_valid_tickets(rules, fields):
    fields = list(map(int, fields.split(",")))
    rep1 = []
    for f in fields:
        rep2 = []
        for r1, r2 in rules:
            if r1[0]<=f<=r1[1] or r2[0]<=f<=r2[1]:
                rep2.append(True)
            else:
                rep2.append(False)

        rep1.append(rep2)
    i_fields = [any(x) for x in rep1]
    for i in range(len(i_fields)):
        if not i_fields[i]:
            return None
    
    return rep1

def find_min(G):
    result_key = None
    for k, v in G.items():
        if len(v) == 1:
            val = list(v)[0]
            result_key = k

    for _, v2 in G.items():
        if val in v2:
            v2.remove(val)
        
    del G[result_key]
    return G, (result_key, val)


if __name__=="__main__":
    RAW = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""

    RAW1 = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9"""

    with open("input.txt", "r") as f:
        X = f.read()

    rules, ticket, nearby_ticket = parse(X)
    rep = 0
    for nt in nearby_ticket:
        w = get_invalid_tickets(rules, nt)
        if w:
            rep += w
    print(rep)
    print(rules)
    #
    # PART 2
    # 
    consolidate = nearby_ticket + ticket
    rep = {a: set() for a in range(len(ticket[0].split(",")))}

    for t in range(len(consolidate)):
        v = get_valid_tickets(rules, consolidate[t])
        if v:
            for i, number in enumerate(v):
                for j, boo_rule in enumerate(number):
                    if not boo_rule:
                        rep[i].add(j)

    possible_entries = {
        a: set() for a in range(len(ticket[0].split(",")))
    }

    filter_set = set()
    for i in range(len(ticket[0].split(","))):
        filter_set.add(i)

    for k, v in rep.items():
        possible_entries[k].update(filter_set.difference(v))

    # print(possible_entries)

    final_dict = {}
    while len(final_dict) < len(ticket[0].split(",")):
        possible_entries, rep =  find_min(possible_entries)
        if rep:
            final_dict[rep[0]] = rep[1]
        print(final_dict)
        # print(possible_entries)
    print(possible_entries)

    ans = 1
    ticket = list(map(int, ticket[0].split(",")))
    print(ticket)
    for y, z in final_dict.items():
        if z in range(6):
            ans *= ticket[y]

    print(ans)