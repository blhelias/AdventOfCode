from collections import namedtuple, Counter
from typing import Dict, List


class Planet:
    """A planet is an object that can have direct
        or indirect orbit"""
    def __init__(self, name):
        self.name = name
        self.orbit = None # only one planet possible !
    
    def search(self):
        counter  = 0
        transfers = [self]

        if self.name == "COM":
            return counter, transfers

        p = self.orbit.planet

        while True:
            counter += 1
            if p.name == "COM":
                return counter, transfers
            else:
                p = p.orbit.planet

            transfers.append(p) 

        return counter, transfers

    def __hash__(self):
        return hash(str(self.name))

    def __eq__(self, other) -> bool:
        return self.name == other.name

    def __repr__(self):
        return "{name} orbits around {orbit} ! ".format(orbit=self.orbit, name=self.name)


class Orbit:
    """an orbit is a set of 2 planet"""
    def __init__(self, planet: Planet) -> None:
        self.planet = planet

    def __repr__(self):
        return self.planet.name


class Map:
    """a map is a set of direct orbit between 2 planets"""
    def __init__(self):
        self.orbit_map = {}
    
    def get_planet(self, planet_name: str):
        # assert planet exists otherwise add it to the map
        if planet_name not in self.orbit_map:
            p = Planet(planet_name)
            self.orbit_map[planet_name] = p
        else:
            p = self.orbit_map[planet_name]

        return p

    def add_orbit(self, etoile: Planet, planet: Planet) -> None:
        v = self.get_planet(planet.name)
        w = self.get_planet(etoile.name)
        v.orbit = Orbit(w)
    
    def build(self, path: str) -> None:
        with open(path) as orbit_graph_file: # disable pylint
            orbit_graph_io = orbit_graph_file.read()
            orbit_graph = orbit_graph_io.split('\n')
            orbit_graph = [line.split(")") for line in orbit_graph]

        for planet_duo in orbit_graph:
            v = self.get_planet(planet_duo[0])
            w = self.get_planet(planet_duo[1])
            self.add_orbit(v, w)


def remove_intersection(list1, list2):
    return list(set(transfer1)^set(transfer2))


if __name__ == "__main__":
    orbit_graph = Map()
    orbit_graph.build("input.txt")
    # pour chaque planet, retracer le nombre d'orbit
    # indirect jusqu'a la planete de base COM
    transfers_list = []
    for planet_name, planet_value in orbit_graph.orbit_map.items():
        if planet_name == "YOU" or planet_name == "SAN":
            total_orbit, transfers = planet_value.search() # specifice a part 2
            transfers_list.append(transfers)
        # reponse += planet_value.search()  # Part 1
    # print(response) 

    transfer1 = transfers_list[0]
    transfer2 = transfers_list[1]

    print(len(remove_intersection(transfer1, transfer2)))