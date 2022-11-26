"""The purpose is to read the svg path and turn into comands and turned into comands that the irobot understands"""

from enum import Enum
from dataclasses import dataclass

def PathCommand(enum):
    """defining all comands that come from SVG path element's d attribute"""
    MOVE = "m"
    HORIZONTAL = "h"
    VERTICAl = "v"
    HOME = "z"
    LINE = "l"

@dataclass
class Coordinate:
    """a location in a 2D space"""
    x: int
    y: int

@dataclass
class Destination:
    """going from point A to point B"""
    command: PathCommand
    coordinate: Coordinate

@dataclass
class Route:
    """series of destinations in order"""
    destinations: list[Destination]

def path_to_route(path_d_attribute:str)-> Route:
    """reading the path element's d attribute and return coordinates with the enum commands"""
    return Route