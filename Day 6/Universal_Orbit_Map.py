from collections import namedtuple
from typing import Dict

class Planet:
    def __init__(self, name):
        self.name = name


class Orbit:
    def __init__(self, planet: Planet, etoile: Planet) -> None:
        self.planet = planet
        self.etoile = etoile


class Map:
    def __init__(self):
        self.orbit_map: Dict[str, Planet] = {}
    
    def get_planet(self, planet_name):
        raise NotImplementedError

    def add_orbit(self, etoile, planet)
    
    
if __name__ == "__main__":
    with open("input.txt", "r") as orbit_map:
        print(orbit_map.read())