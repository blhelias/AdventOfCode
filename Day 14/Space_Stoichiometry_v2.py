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
        chemical, qty = raw.strip().split(" ")
        return Amount(chemical, qty)


def parse_input(obj: str):
    s = obj.split(" => ")
    right = s[1].split(" ")
    left = s[0].split(", ")
    input_amount = [Amount.from_string(l) for l in left]
    output_amount = Amount(right[1], right[0])
    return Rule(input_amount, output_amount)


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
    i = TEST1.split("\n")
    print(i)
    p = [parse_input(raw) for raw in i]
