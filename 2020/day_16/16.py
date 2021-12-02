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
            [int(left.split("-")[0]), int(left.split("-")[1])],
            [int(right.split("-")[0]), int(right.split("-")[1])],
        )
        return rule


class Note(NamedTuple):
    rules: List[Rule]
    ticket: List[int]
    nearby_ticket: List[List[int]]


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
    return Note(
        rule,
        list(map(int, t[0].split(","))),
        [list(map(int, nt.split(","))) for nt in nearby_t],
    )


def get_invalid_tickets(rules, fields):
    M = []
    for f in fields:
        m = []
        for r1, r2 in rules:
            if r1[0] <= f <= r1[1] or r2[0] <= f <= r2[1]:
                m.append(True)
            else:
                m.append(False)

        M.append(m)

    i_fields = [any(x) for x in M]

    for i in range(len(i_fields)):
        if not i_fields[i]:
            return fields[i]

    return 0


def get_valid_tickets(rules, fields):
    M = []
    for f in fields:
        m = []
        for r1, r2 in rules:
            if r1[0] <= f <= r1[1] or r2[0] <= f <= r2[1]:
                m.append(True)
            else:
                m.append(False)

        M.append(m)
    i_fields = [any(x) for x in M]
    for i in range(len(i_fields)):
        if not i_fields[i]:
            return None

    return M


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


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        X = f.read()

    rules, ticket, nearby_ticket = parse(X)
    #
    # PART 1
    #
    p1 = sum(get_invalid_tickets(rules, nt) for nt in nearby_ticket)
    print(p1)

    #
    # PART 2
    #
    rep = {a: set() for a in range(len(ticket))}

    for row in range(len(nearby_ticket)):
        valid = get_valid_tickets(rules, nearby_ticket[row])
        if valid:
            for i, number in enumerate(valid):
                for j, boolean_rule in enumerate(number):
                    if not boolean_rule:
                        rep[i].add(j)

    possible_entries = {a: set() for a in range(len(ticket))}

    filter_set = set([i for i in range(len(ticket))])

    for k, v in rep.items():
        possible_entries[k].update(filter_set.difference(v))

    final_dict = {}
    while len(final_dict) < len(ticket):
        possible_entries, rep = find_min(possible_entries)
        final_dict[rep[0]] = rep[1]

    ans = 1
    ticket = list(map(int, ticket))
    for y, z in final_dict.items():
        if z in range(6):
            ans *= ticket[y]

    print(ans)
