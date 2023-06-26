from irobot.robot_navigation import Point, LineSegment, Tracking
import math

''' can never have negative degree angles '''

""" upper right quad """

def test_up_PP():
    start = Point(1,1)
    destination = Point(1,5)
    segment = LineSegment(start, destination)
    assert segment.angle == 0
    assert segment.distance == 4

def test_down_PP():
    start = Point(1,4)
    destination = Point(1,2)
    segment = LineSegment(start, destination)
    assert segment.angle == 180
    assert segment.distance == 2

def test_left_PP():
    start = Point(6,5)
    destination = Point(1,5)
    segment = LineSegment(start, destination)
    assert segment.angle == 270
    assert segment.distance == 5

def test_right_PP():
    start = Point(1,4)
    destination = Point(5,4)
    segment = LineSegment(start, destination)
    assert segment.angle == 90
    assert segment.distance == 4

def test_up_right_PP():
    start = Point(1,4)
    destination = Point(5,9)
    segment = LineSegment(start, destination)
    assert segment.angle == 38.7
    assert segment.distance == 6.4

def test_down_right_PP():
    start = Point(1,9)
    destination = Point(5,4)
    segment = LineSegment(start, destination)
    assert segment.angle == 141.3
    assert segment.distance == 6.4

def test_up_left_PP():
    start = Point(5,4)
    destination = Point(1,9)
    segment = LineSegment(start, destination)
    assert segment.angle == 321.3
    assert segment.distance == 6.4

def test_down_left_PP():
    start = Point(5,9)
    destination = Point(1,4)
    segment = LineSegment(start, destination)
    assert segment.angle == 218.7
    assert segment.distance == 6.4

"""lowwer right quad"""

def test_up_PN():
    start = Point(1,-5)
    destination = Point(1,-1)
    segment = LineSegment(start, destination)
    assert segment.angle == 0
    assert segment.distance == 4

def test_down_PN():
    start = Point(1,-2)
    destination = Point(1,-4)
    segment = LineSegment(start, destination)
    assert segment.angle == 180
    assert segment.distance == 2

def test_left_PN():
    start = Point(6,-5)
    destination = Point(1,-5)
    segment = LineSegment(start, destination)
    assert segment.angle == 270
    assert segment.distance == 5

def test_right_PN():
    start = Point(1,-4)
    destination = Point(5,-4)
    segment = LineSegment(start, destination)
    assert segment.angle == 90
    assert segment.distance == 4

def test_up_right_PN():
    start = Point(1,-9)
    destination = Point(5,-4)
    segment = LineSegment(start, destination)
    assert segment.angle == 38.7
    assert segment.distance == 6.4


def test_down_right_PN():
    start = Point(1,-4)
    destination = Point(5,-9)
    segment = LineSegment(start, destination)
    assert segment.angle == 141.3
    assert segment.distance == 6.4

def test_up_left_PN():
    start = Point(5,-9)
    destination = Point(1,-4)
    segment = LineSegment(start, destination)
    assert segment.angle == 321.3
    assert segment.distance == 6.4

def test_down_left_PN():
    start = Point(5,-4)
    destination = Point(1,-9)
    segment = LineSegment(start, destination)
    assert segment.angle == 218.7
    assert segment.distance == 6.4

"""Lower left quad"""

def test_up_NN():
    start = Point(-1,-5)
    destination = Point(-1,-1)
    segment = LineSegment(start, destination)
    assert segment.angle == 0
    assert segment.distance == 4

def test_down_NN():
    start = Point(-1,-2)
    destination = Point(-1,-4)
    segment = LineSegment(start, destination)
    assert segment.angle == 180
    assert segment.distance == 2

def test_left_NN():
    start = Point(-1,-5)
    destination = Point(-6,-5)
    segment = LineSegment(start, destination)
    assert segment.angle == 270
    assert segment.distance == 5

def test_right_NN():
    start = Point(-5,-4)
    destination = Point(-1,-4)
    segment = LineSegment(start, destination)
    assert segment.angle == 90
    assert segment.distance == 4

def test_up_right_NN():
    start = Point(-5,-9)
    destination = Point(-1,-4)
    segment = LineSegment(start, destination)
    assert segment.angle == 38.7
    assert segment.distance == 6.4


def test_down_right_NN():
    start = Point(-5,-4)
    destination = Point(-1,-9)
    segment = LineSegment(start, destination)
    assert segment.angle == 141.3
    assert segment.distance == 6.4

def test_up_left_NN():
    start = Point(-1,-9)
    destination = Point(-5,-4)
    segment = LineSegment(start, destination)
    assert segment.angle == 321.3
    assert segment.distance == 6.4

def test_down_left_NN():
    start = Point(-1,-4)
    destination = Point(-5,-9)
    segment = LineSegment(start, destination)
    assert segment.angle == 218.7
    assert segment.distance == 6.4

"""Upper left quad"""

def test_up_NP():
    start = Point(-1,1)
    destination = Point(-1,5)
    segment = LineSegment(start, destination)
    assert segment.angle == 0
    assert segment.distance == 4

def test_down_NP():
    start = Point(-1,4)
    destination = Point(-1,2)
    segment = LineSegment(start, destination)
    assert segment.angle == 180
    assert segment.distance == 2

def test_left_NP():
    start = Point(-1,5)
    destination = Point(-6,5)
    segment = LineSegment(start, destination)
    assert segment.angle == 270
    assert segment.distance == 5

def test_right_NP():
    start = Point(-5,4)
    destination = Point(-1,4)
    segment = LineSegment(start, destination)
    assert segment.angle == 90
    assert segment.distance == 4

def test_up_right_NP():
    start = Point(-5,4)
    destination = Point(-1,9)
    segment = LineSegment(start, destination)
    assert segment.angle == 38.7
    assert segment.distance == 6.4


def test_down_right_NP():
    start = Point(-5,9)
    destination = Point(-1,4)
    segment = LineSegment(start, destination)
    assert segment.angle == 141.3
    assert segment.distance == 6.4

def test_up_left_NP():
    start = Point(-1,4)
    destination = Point(-5,9)
    segment = LineSegment(start, destination)
    assert segment.angle == 321.3
    assert segment.distance == 6.4

def test_down_left_NP():
    start = Point(-1,9)
    destination = Point(-5,4)
    segment = LineSegment(start, destination)
    assert segment.angle == 218.7
    assert segment.distance == 6.4

""" Spanning Quads """

def test_spanning_PP_to_NN():
    start = Point(1,9)
    destination = Point(-5,-4)
    segment = LineSegment(start, destination)
    assert segment.angle == 204.8
    assert segment.distance == 14.3

# def test_course():
#     line1 = LineSegment(Point(0, 0), Point(0, 1))
#     line2 = LineSegment(Point(0, 1), Point(1, 1))
#     line3 = LineSegment(Point(1, 1), Point(0, 0))
#     lines = [line1, line2, line3]
#     x, y, direction = course(lines)
#     assert x == 0
#     assert y == 0
#     assert direction == 225

def test_tracking_construction():
    """Making sure what is assigned in cunstruction is what is to be confirmed of the current heding/values"""
    expected_x = 1
    expected_y = 5
    expected_dir = 45
    track = Tracking(expected_x, expected_y, expected_dir)
    assert track.x == expected_x
    assert track.y == expected_y
    assert track.direction == expected_dir

def test_tracking_first_quad():
    """turn 90 deg from the center origin(0,0)"""
    point = Point(5, 0)
    direction = 90
    origin_y = 0
    track = Tracking(0, origin_y, 0)
    track.update_position(point, direction)
    assert track.x == point.x
    assert track.y == point.y
    assert  track.direction == direction

def test_tracking_south_full_reversal():
    """facing down and turn around"""

def test_course_first_quad():
    """test from (0,0) to (1,1)"""
    line = LineSegment(Point(0,0), Point(1,1))
    track = Tracking(0,0,0)
    track.course([line])
    assert track.x == 1
    assert track.y == 1
    assert track.direction == 45

# def test_course_first_quad_return_origin():
#     line = LineSegment(Point(1,1), Point(0,0))
#     track = Tracking(1,1,45)
#     track.course([line])
#     assert track.x == 0
#     assert track.y ==0
#     assert track.direction == 225