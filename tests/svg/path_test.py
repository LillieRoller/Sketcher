from sketcher.svg.path import path_to_route, Route, Destination, Coordinate, PathCommand

square_path_fixture = "M 10 10 H 90 V 90 H 10 Z"

def test_path_to_route_square_path():
    # route = path_to_route(square_path_fixture)
    assert False

def test_path_to_route_move_to_destination():
    actual = path_to_route(path_d_attribute = "M 0 0")
    assert len(actual.destinations) == 1

def test_path_to_route_no_destination():
    actual = path_to_route(path_d_attribute = "")
    assert len(actual.destinations) == 0