import math
from typing import List, Dict, NamedTuple, Tuple

class Fuel:
    def __init__(self, fuel: str, quantity, children):
        self.fuel = fuel
        self.quantity = quantity
        self.children = children
        self.require = 0
    
    def key(self):
        return self.fuel
    
    def __repr__(self):
        return self.fuel + ":: q: " + self.quantity + ", chidren: " + str(self.children) + ", require: "+str(self.require)
    
class Map:
    def __init__(self, f_map: Dict[str, Fuel]):
        self.f_map = f_map
    
    def get_node(self, name: str) -> Fuel:
        try:
            return self.f_map[name]
        except KeyError:
            return None

    def compute(self, start_name: str):
        self.stack = []
        start_n = self.get_node(start_name)
        for child in start_n.children:
            n = self.get_node(child[1])
            n.require += int(start_n.quantity)
            self.stack.append(child)

        while len(self.stack) > 0:
            obj = self.stack.pop()
            n = self.get_node(obj[1])
            if n:
                n.require += int(obj[0])

                for c in n.children:
                    self.stack.append(c)
        
        ore_fuel = [v for k,v in self.f_map.items() if "ORE" in [n[1] for n in v.children]]

        cnt = 0
        for fuel in ore_fuel:
            cnt += math.ceil(fuel.require / int(fuel.quantity)) * int(fuel.quantity)

        return cnt


def parse_input(input_code: str):
    map_fuel = {}
    code = input_code.split("\n")
    for line in code:
        l = line.split(" => ")
        left = l[0].split(", ")
        parent_fuel = l[1].split(" ")
        q = parent_fuel[0]
        parent_name = parent_fuel[1]

        children=[]
        for i in left:
            c_fuel = i.split(" ")
            children.append((c_fuel[0], c_fuel[1]))
        
        map_fuel[parent_name] = Fuel(parent_name, q, children)
    return map_fuel

if __name__ == "__main__":
    TEST_CODE_1 = """9 ORE => 2 A
8 ORE => 3 B
7 ORE => 5 C
3 A, 4 B => 1 AB
5 B, 7 C => 1 BC
4 C, 1 A => 1 CA
2 AB, 3 BC, 4 CA => 1 FUEL"""
    G = Map(parse_input(TEST_CODE_1))
    part1 = G.compute("FUEL")