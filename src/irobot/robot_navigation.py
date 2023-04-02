from dataclasses import dataclass
import math
import numpy as np

@dataclass
class Point:
    """two dimentional coordinant of x horizontal and y vertical
    unit of meassurment for x and y is up to the math defined"""
    x: int
    y: int

class LineSegment:
    """provides the dtails to navigate from start to destination"""
    def __init__(self, start:Point, destination:Point) -> None:
        run = destination.x - start.x
        rise = destination.y - start.y
        hypo = run**2 + rise**2
        hypotenuse = math.sqrt(hypo)
        sin_theta = rise / hypotenuse
        inverse_sin_rad = np.arcsin(sin_theta)
        inverse_sin_deg = math.degrees(inverse_sin_rad)
        angle_degree = 90 - inverse_sin_deg
        self.angle = int(angle_degree)
        self.distance = int(hypotenuse)