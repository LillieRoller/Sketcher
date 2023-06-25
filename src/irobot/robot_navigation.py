from dataclasses import dataclass
import math
import numpy as np

@dataclass
class Point:
    """two dimentional coordinant of x horizontal and y vertical
    unit of meassurment for x and y is up to the math defined"""
    x: int
    y: int

def angle_formula(run: float, rise: float, hypot: float) -> float:
    """calculate the angle to navigate the distance. 
    Robot wants angle degree from North 
    """
    # cos α = [b2 + c2 – a2]/2bc
    # α = cos-1 (b^2+c^2-a^2)/2bc
    # α = cos-1 (hypo^2+rise^2-run^2)/2(hypo)(rise)
    step1 = hypot ** 2 + rise ** 2 - run ** 2
    step2 = step1 / (2 * hypot * rise)
    inverse_cos_rad = np.arccos(step2)
    inverse_cos_deg = math.degrees(inverse_cos_rad)
    return round(inverse_cos_deg, 1)

class LineSegment:
    """provides the details to navigate from start to destination
    
    y = rise    d = distance (hyptonenuse)
            
            | A/ destination
            | /
            |/ start 
      ---------------  x = run
            |
            |
            |
    From a start of x,y within the grid, the robot wants angle from North 
    and distance to travel. 
    Pythagorean theorum solves for d.
    A uses law of sines/cosines.


    """

    def __init__(self, start:Point, destination:Point) -> None:
        self.angle:int = None
        self.distance:int = None
        self.start:Point = start
        self.destination:Point = destination
        # solving distance using pythagorean theorum (hypotenuse)
        run = int(destination.x - start.x)
        rise = int(destination.y - start.y)
        hypo = run**2 + rise **2
        hypot = math.sqrt(hypo)
        hypotenuse = round(hypot, 1)
        self.distance = hypotenuse
        
        # direct right special case avoids divide by zero
        if rise == 0 and run > 0:
            self.angle = 90
        # direct left special case avoids divide by zero
        elif rise == 0 and run < 0:
            self.angle = 270
        elif run < 0 and rise > 0:
            self.angle = 360 - angle_formula(run=run,rise=rise,hypot=hypot)
        elif run < 0 and rise < 0:
            self.angle = 360 - angle_formula(run=run,rise=rise,hypot=hypot)
        else:
            self.angle = angle_formula(run=run,rise=rise,hypot=hypot)
            # raise NotImplementedError(f"Not yet handling {start} and {destination}")


       

            

        

        # if start.x < destination.x and start.y < destination.y or start.x < destination.x and start.y > destination.y:
        #     final_angle = inverse_cos_deg
        # elif start.x > destination.x and start.y > destination.y or start.x > destination.x and start.y < destination.y:
        #     counter_clockwise_angle = inverse_cos_deg
        #     final_angle = 360 - counter_clockwise_angle
        
        # elif start.x == destination.x and start.y > destination.y:
        #     final_angle = 180
        # elif start.x == destination.x and start.y < destination.y:
        #     final_angle = 0
        
        # elif start.x > destination.x and start.y == destination.y:
        #     final_angle = 270
        # elif start.x < destination.x and start.y == destination.y:
        #     final_angle = 90

        # self.angle = int(final_angle)
        # self.distance = int(hypotenuse)
        # self.start = start
        # self.destination = destination

    def __str__(self) -> str:
        return f"{self.angle} {self.distance}"

class Tracking:
    """tracks the robot and its current position and direction"""
    x:int = None
    y:int = None
    direction:int = None
    def __init__(self, x: int, y: int, dir: int) -> None:
        self.x = x
        self.y = y
        self.direction = dir

    def update_position(self, point: Point, dir: int) -> None:
        """updates the robot's position and direction based on a positioning
        not taking the direction ther distance  but about the point"""
        # update direction
        self.x = point.x
        self.y = point.y

        # calculate new position
        
        self.direction = dir + self.direction

    def course(self, path: list[LineSegment]) -> None:
        """keeps track of the position and direction of the robot as it moves along the path"""

        for segment in path:
            # update robot position and direction based on segment
            self.update_position(point = segment.destination, dir = segment.angle)
        
class RobotNavigator:
    """Takes points and moves to diffferent coordinante buy using rotate and distance packets together """