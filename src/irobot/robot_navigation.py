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
    """provides the details to navigate from start to destination"""
    def __init__(self, start:Point, destination:Point) -> None:
        run = int(destination.x - start.x)
        rise = int(destination.y - start.y)
        hypo = run**2 + rise**2
        hypotenuse = math.sqrt(hypo)        
        step1 = (run**2) - (hypotenuse**2) - (rise**2)
        step2 = 2*rise*hypotenuse
        if step2 == 0:
            step3 = 0
            inverse_cos_rad = np.arccos(step3)
            inverse_cos_deg = 90
        else:
            step3 = -1*(step1/step2)
            inverse_cos_rad = np.arccos(step3)
            inverse_cos_deg = math.degrees(inverse_cos_rad)
        angle = round(inverse_cos_deg)
        if destination.x < 0:
            adjust_angle = 360 - angle
            final_angle = adjust_angle
        else:
            final_angle = angle
        self.angle = int(final_angle)
        self.distance = int(hypotenuse)

    def __str__(self) -> str:
        return f"{self.angle} {self.distance}"