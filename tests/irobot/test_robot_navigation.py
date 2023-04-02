from irobot.robot_navigation import Point, LineSegment
import math

def test_verticle_line():
    start = Point(0,0)
    destination = Point(0,1)
    segment = LineSegment(start, destination)
    assert segment.angle == 0
    assert segment.distance == 1

def test_horizontal_line():
    start = Point(0,0)
    destination = Point(1, 0)
    segment = LineSegment(start, destination)
    assert segment.angle == 90
    assert segment.distance == 1

def test_diagonal_line():
    start = Point(0,0)
    destination = Point(1, 1)
    segment = LineSegment(start, destination)
    assert segment.angle == int(45)
    assert segment.distance == int(math.sqrt(2))

def test_sw_diagonal_line():
    start = Point(0,0)
    destination = Point(-1,-1)
    segment = LineSegment(start, destination)
    assert segment.angle == int(-135)
    assert segment.distance == int(math.sqrt(2))

def test_nw_diagonal_line():
    start = Point(0,0)
    destination = Point(-1,1)
    segment = LineSegment(start, destination)
    assert segment.angle == int(-45)
    assert segment.distance == int(math.sqrt(2))