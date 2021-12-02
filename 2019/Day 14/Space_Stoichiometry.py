import math
import copy
from typing import List, Dict, NamedTuple, Tuple


class Fuel:
    def __init__(self, fuel: str, quantity, children, needs):
        self.fuel = fuel
        self.quantity = quantity
        self.children = children
        self.needs = needs
        self.require = 0

    def key(self):
        return self.fuel

    def __repr__(self):
        return f"{self.quantity} {self.fuel} needs {self.children}, require= {self.require}"


class Map:
    def __init__(self):
        self.f_map = {}
        self.remainder = {}

    def get_node(self, name: str) -> Fuel:
        try:
            return self.f_map[name]
        except KeyError:
            return None

    def parse_input(self, input_code: str) -> None:
        code = input_code.split("\n")

        for line in code:
            l = line.split(" => ")
            left = l[0].split(", ")
            parent_fuel = l[1].split(" ")
            q = int(parent_fuel[0])
            parent_name = parent_fuel[1]

            children = []
            needs = []
            for i in left:
                c_fuel = i.split(" ")
                children.append([int(c_fuel[0]), c_fuel[1]])
                needs.append((int(c_fuel[0]), c_fuel[1]))

            self.f_map[parent_name] = Fuel(parent_name, q, children, needs)

    def reset_require(self):
        for k, fuel in self.f_map.items():
            fuel.require = 0

    def reset_children(self):
        for k, fuel in self.f_map.items():
            fuel.children = [[c[0], c[1]] for c in fuel.needs]

    def run(self):

        while len(self.stack) > 0:
            obj = self.stack.pop()
            n = self.get_node(obj[1])

            if n:

                n.require += (obj[0] + self.remainder[obj[1]][0]) // n.quantity
                self.remainder[obj[1]][0] = (
                    obj[0] + self.remainder[obj[1]][0]
                ) % n.quantity

                for idx, c in enumerate(n.children):
                    if c[1] != "ORE":
                        c_cp = copy.deepcopy(c)
                        c_cp[0] = n.needs[idx][0] * n.require
                        self.stack.insert(0, c_cp)

            print(n)
            print(obj)
            print()

        print(self.remainder)

    def results(self):
        ore_fuel = [
            v for k, v in self.f_map.items() if "ORE" in [n[1] for n in v.children]
        ]

        cnt = 0
        for fuel in ore_fuel:
            cnt += fuel.require * fuel.needs[0][0]

        return cnt

    def compute(self, start_name: str):
        self.remainder = {k: [0, 0] for k, _ in self.f_map.items()}

        self.stack = []
        start_n = self.get_node(start_name)

        for child in start_n.children:
            n = self.get_node(child[1])
            self.stack.append(child)

        running = True
        count = 0
        step = 0
        while running:

            self.run()
            count += self.results()
            print(count)

            self.reset_require()
            self.reset_children()

            c = 0
            for k, v in self.remainder.items():

                f = self.get_node(k)

                if v[0] != 0 and v[1] == 0:
                    c += 1
                    self.stack.append([f.quantity, k])
                    v[1] += v[0]
                    v[0] = 0

                elif v[0] + v[1] <= f.quantity:
                    v[1] = (v[1] + v[0]) % f.quantity
                    v[0] = 0

                elif v[0] + v[1] > f.quantity:
                    c += 1
                    self.stack.append([f.quantity, k])
                    v[1] = (v[0] + v[1]) - f.quantity
                    v[0] = 0

            if c == 0 and step >= 1:
                running = False

            step += 1
        return count


if __name__ == "__main__":
    TEST_CODE_1 = """9 ORE => 2 A
8 ORE => 3 B
7 ORE => 5 C
3 A, 4 B => 1 AB
5 B, 7 C => 1 BC
4 C, 1 A => 1 CA
2 AB, 3 BC, 4 CA => 1 FUEL"""

    TEST_CODE_2 = """157 ORE => 5 NZVS
165 ORE => 6 DCFZ
44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
179 ORE => 7 PSHF
177 ORE => 5 HKGWZ
7 DCFZ, 7 PSHF => 2 XJWVT
165 ORE => 2 GPVTF
3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT"""

    TEST_CODE_3 = """2 VPVL, 7 FWMGM, 2 CXFTF, 11 MNCFX => 1 STKFG
17 NVRVD, 3 JNWZP => 8 VPVL
53 STKFG, 6 MNCFX, 46 VJHF, 81 HVMC, 68 CXFTF, 25 GNMV => 1 FUEL
22 VJHF, 37 MNCFX => 5 FWMGM
139 ORE => 4 NVRVD
144 ORE => 7 JNWZP
5 MNCFX, 7 RFSQX, 2 FWMGM, 2 VPVL, 19 CXFTF => 3 HVMC
5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF => 6 GNMV
145 ORE => 6 MNCFX
1 NVRVD => 8 CXFTF
1 VJHF, 6 MNCFX => 4 RFSQX
176 ORE => 6 VJHF"""
    TEST_CODE_4 = """171 ORE => 8 CNZTR
7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => 4 PLWSL
114 ORE => 4 BHXH
14 VRPVC => 6 BMBT
6 BHXH, 18 KTJDG, 12 WPTQ, 7 PLWSL, 31 FHTLT, 37 ZDVW => 1 FUEL
6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP => 6 FHTLT
15 XDBXC, 2 LTCX, 1 VRPVC => 6 ZLQW
13 WPTQ, 10 LTCX, 3 RJRHP, 14 XMNCP, 2 MZWV, 1 ZLQW => 1 ZDVW
5 BMBT => 4 WPTQ
189 ORE => 9 KTJDG
1 MZWV, 17 XDBXC, 3 XCVML => 2 XMNCP
12 VRPVC, 27 CNZTR => 2 XDBXC
15 KTJDG, 12 BHXH => 5 XCVML
3 BHXH, 2 VRPVC => 7 MZWV
121 ORE => 7 VRPVC
7 XCVML => 6 RJRHP
5 BHXH, 4 VRPVC => 5 LTCX"""

    G = Map()
    G.parse_input(TEST_CODE_3)
    part1 = G.compute("FUEL")
