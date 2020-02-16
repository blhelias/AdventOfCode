# the code was copied from https://www.youtube.com/watch?v=soZ0pzeGbvo
import math
from typing import List, NamedTuple
from collections import namedtuple

class Rule(NamedTuple):
    input: List['Amount']
    output: 'Amount'


class Amount(NamedTuple):
    chemical: str
    quantity: int

    @staticmethod
    def from_string(raw: str) -> 'Amount':
        qty, chemical = raw.strip().split(" ")
        return Amount(chemical, int(qty))

def parse_rule(obj: str):
    s = obj.split(" => ")
    right = s[1].split(" ")
    left = s[0].split(", ")
    input_amount = [Amount.from_string(l) for l in left]
    output_amount = Amount(right[1], int(right[0]))
    return Rule(input_amount, output_amount)

def least_ore(rules: List[Rule], fuel_q):
    rules_by_product = {rule.output.chemical: rule for rule in rules}
    ore_needed = 0
    rep = 0

    requirements = {"FUEL": fuel_q}

    def done() -> bool:
        return  all(qty <= 0 for qty in requirements.values())

    while not done():
        key = next(iter(chem for chem, qty in requirements.items() if qty > 0))
        qty_needed = requirements[key]

        rule = rules_by_product[key]
        num_times = math.ceil(qty_needed / rule.output.quantity)
        requirements[key] -= num_times * rule.output.quantity

        for amount in rule.input:
            if amount.chemical == "ORE":
                ore_needed += amount.quantity * num_times
            else:
                requirements[amount.chemical] = requirements.get(amount.chemical, 0) + num_times * amount.quantity

    return ore_needed


if __name__ == "__main__":
    TEST1 = """157 ORE => 5 NZVS
165 ORE => 6 DCFZ
44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
179 ORE => 7 PSHF
177 ORE => 5 HKGWZ
7 DCFZ, 7 PSHF => 2 XJWVT
165 ORE => 2 GPVTF
3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT"""

    # rules = [parse_rule(raw) for raw in TEST1.split("\n")]
    # print(least_ore(rules))

    with open("input.txt", 'r') as t:
        TEST = t.read()

    rules = [parse_rule(raw) for raw in TEST.split("\n")]
    fuel_q = range(1863000,1864100)

    print(least_ore(rules, 1863741))
    print(least_ore(rules, 1863742))
