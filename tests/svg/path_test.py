from sketcher.svg.path import path_to_route, Route, Segment, Coordinate, SegmentType

square_path_fixture = "M 1 2 H 90 V 90 H 1 Z"


def test_path_to_route_square_path():
    actual = path_to_route(path_d_attribute = square_path_fixture)
    assert len(actual.segments) == 5
    segment1 = actual.segments[0]
    segment2 = actual.segments[1]
    segment3 = actual.segments[2]
    segment4 = actual.segments[3]
    segment5 = actual.segments[4]
    assert segment1.type == SegmentType.MOVE
    assert segment1.coordinate.x == 1
    assert segment1.coordinate.y == 2
    assert segment2.type == SegmentType.LINE
    assert segment2.coordinate.x == 90
    assert segment2.coordinate.y == 2
    assert segment3.type == SegmentType.LINE
    assert segment3.coordinate.x == 90
    assert segment3.coordinate.y == 90
    assert segment4.type == SegmentType.LINE
    assert segment4.coordinate.x == 1
    assert segment4.coordinate.y == 90
    assert segment5.type == SegmentType.LINE
    assert segment5.coordinate.x == 1
    assert segment5.coordinate.y == 2

def test_path_to_route_no_destination():
    actual = path_to_route(path_d_attribute = "")
    assert len(actual.segments) == 0