from irobot.robot_navigation import Point, LineSegment, Tracking, course
import math

''' can never have negative degree angles '''

def test_up():
    start = Point(0,0)
    destination = Point(0,1)
    segment = LineSegment(start, destination)
    assert segment.angle == int(0)
    assert segment.distance == int(1)

def test_up_right():
    start = Point(0, 0)
    destination = Point(1, 1)
    segment = LineSegment(start, destination)
    assert segment.angle == int(45)
    assert segment.distance == int(math.sqrt(2))

def test_right():
    start = Point(0, 0)
    destination = Point(1, 0)
    segment = LineSegment(start, destination)
    assert segment.angle == int(90)
    assert segment.distance == int(1)

def test_right_down():
    start = Point(0, 0)
    destination = Point(1, -1)
    segment = LineSegment(start, destination)
    assert segment.angle == int(135)
    assert segment.distance == int(math.sqrt(2))

def test_down():
    start = Point(0, 0)
    destination = Point(0, -1)
    segment = LineSegment(start, destination)
    assert segment.angle == int(180)
    assert segment.distance == int(1)

def test_down_left():
    start = Point(0,0)
    destination = Point(-1,-1)
    segment = LineSegment(start, destination)
    assert segment.angle == int(225)
    assert segment.distance == int(math.sqrt(2))

def test_left():
    start = Point(0, 0)
    destination = Point(-1,0)
    segment = LineSegment(start, destination)
    assert segment.angle == int(270)
    assert segment.distance == int(1)

def test_left_up():
    start = Point(0, 0)
    destination = Point(-1, 1)
    segment = LineSegment(start, destination)
    assert segment.angle == int(315)
    assert segment.distance == int(math.sqrt(2))

def test_line_segment():
    p1 = Point(0, 0)
    p2 = Point(1, 1)
    line_seg = LineSegment(p1, p2)
    assert line_seg.angle == 45
    assert line_seg.distance == int(math.sqrt(2))

def test_course():
    line1 = LineSegment(Point(0, 0), Point(0, 1))
    line2 = LineSegment(Point(0, 1), Point(1, 1))
    line3 = LineSegment(Point(1, 1), Point(0, 0))
    lines = [line1, line2, line3]
    x, y, direction = course(lines)
    assert x == 0
    assert y == 0
    assert direction == 225

