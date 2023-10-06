"""The main program to run with python.
	ex: python3 sketcher/sketcher.py
"""
from svg.path import path_to_route, Route, Segment, Coordinate, SegmentType
from irobot.codelevel3 import navigate_to, set_marker, Marker
import irobot.ble_connection as ble_connection
from irobot.robot_navigation import Point
import sys
from svg.path import parse_path
import xml.etree.ElementTree as ET

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

def svg_path_from_file(file_path):
	"""Reads an SVG file and returns the path as a string."""
	# Parse the SVG file
	tree = ET.parse(file_path)
	root = tree.getroot()

	# Find the path element and get the value of its 'd' attribute
	path_element = root.find('.//{http://www.w3.org/2000/svg}path')
	d_attribute = path_element.get('d')

	print("Contents of the 'd' attribute:", d_attribute)
	return d_attribute

def main():
	"""Puts together all that is needed to complete a drawing."""
	args = sys.argv[1:]
	if len(args) == 0:
		print("Error: Must pass the path to the svg file as the first argument DUMBY")
		sys.exit(1)
	file_path = args[0]
	# print(F"Reading the path from {file_path}")
	# path = "M 0 0 H 16 V 16 H 0 L 0 0"  # Example SVG path
	path = svg_path_from_file(file_path)
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