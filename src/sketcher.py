"""The main program to run with python.
	ex: python3 sketcher/sketcher.py
"""
from svg.path import path_to_route, Route, Segment, Coordinate, SegmentType
from irobot.codelevel3 import navigate_to, set_marker, Marker
import irobot.ble_connection as ble_connection
from irobot.robot_navigation import Point

# def convert_path_to_points(path:str):
#     """Converts an SVG path to a list of points."""
#     route = path_to_route(path_d_attribute=path)
#     points = []
#     for segment in route.segments:
#         if segment.type == SegmentType.MOVE:
#             points.append(Point(segment.coordinate.x, segment.coordinate.y))
#         elif segment.type == SegmentType.LINE:
#             points.append(Point(segment.coordinate.x, segment.coordinate.y))
#     return points
def convert_path_to_points(path:str):
    """Converts an SVG path to a list of points."""
    route = path_to_route(path_d_attribute=path)
    points = []
    for segment in route.segments:
        if segment.type == SegmentType.MOVE:
            points.append(Point(segment.coordinate.x, segment.coordinate.y))
        elif segment.type == SegmentType.LINE:
            points.append(Point(segment.coordinate.x, segment.coordinate.y))
    return points

def main():
	"""Puts together all that is needed to complete a drawing."""
	path = "M 0 0 H 16 V 16 H 0 L 0 0"  # Example SVG path
	points = convert_path_to_points(path)
	print(points)  # Or pass 'points' to the robot for further processing
	# points=[
	# Point(16,16),
	# Point(16,-16),
	#  (-16,-16),
	# Point(-16,16),
	# Point(16,16),
	# Point(0,0),
	# ]
	ble_connection.run(points)

if __name__ == "__main__":
    main()