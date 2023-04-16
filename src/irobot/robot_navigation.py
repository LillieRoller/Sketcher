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

class Tracking:
    """tracks the robot and its current position and direction"""
    def __init__(self, x: int, y: int, direction: int) -> None:
        self.x = x
        self.y = y
        self.direction = direction

    def update_position(self, distance: int, angle: int) -> None:
        """updates the robot's position and direction based on a positioning"""
        # update direction
        self.direction += angle
        self.direction %= 360

        # calculate new position
        dx = int(distance * math.cos(math.radians(self.direction)))
        dy = int(distance * math.sin(math.radians(self.direction)))
        new_x = self.x + dx
        new_y = self.y + dy
        return new_x, new_y

def course(path: list[LineSegment]) -> tuple[int, int, int]:
    """keeps track of the position and direction of the robot as it moves along the path"""
    track = Tracking(0,0,0)  # initialize robot position and direction

    for segment in path:
        # update robot position and direction based on segment
        track.update_position(segment.distance, segment.angle)

    # return current position and direction
    return track.x, track.y, track.direction
