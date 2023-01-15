"""The purpose is to read the svg path and turn into comands and turned into comands that the irobot understands"""

from enum import Enum
from dataclasses import dataclass
from svgpathtools import Path, Line, parse_path

class SegmentType(Enum):
    """defining all comands that come from SVG path element's d attribute"""
    MOVE = "move"
    LINE = "line"

@dataclass
class Coordinate:
    """a location in a 2D space"""
    x: int
    y: int

@dataclass
class Segment:
    """going from point A to point B"""
    type: SegmentType
    coordinate: Coordinate

@dataclass
class Route:
    """series of destinations in order"""
    segments: list[Segment]

def path_to_route(path_d_attribute:str)-> Route:
    """reading the path element's d attribute and return coordinates with the enum commands"""
    dests = []
    path = parse_path(path_d_attribute)
    for index, line in enumerate(path):

        # move to the start of the first segment only for the first segment
        if index == 0:
            coordinate = Coordinate(x = line.start.real, y = line.start.imag)
            segment = Segment(type = SegmentType.MOVE, coordinate=coordinate)
            dests.append(segment)

        # draw line to the end of each segment
        coordinate = Coordinate(x = line.end.real, y = line.end.imag)
        segment = Segment(type = SegmentType.LINE, coordinate=coordinate)
        dests.append(segment)

    return Route(segments=dests)