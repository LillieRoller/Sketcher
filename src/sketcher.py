"""The main program to run with python.
	ex: python3 sketcher/sketcher.py
"""
from svg.path import path_to_route, Route, Segment, Coordinate, SegmentType
from irobot.codelevel3 import navigate_to, set_marker, Marker
import irobot.ble_connection as ble_connection
from irobot.robot_navigation import Point

def draw_path(path:str):
	"""will recieve a svg path and draw the path commands"""
	route = path_to_route(path_d_attribute = path)
	for segment in route.segments:
		if segment.type == SegmentType.MOVE:
			print(set_marker(Marker.UP))
		elif segment.type == SegmentType.LINE:
			print(set_marker(Marker.DOWN))
		
		print(navigate_to(x = segment.coordinate.x, y = segment.coordinate.y))



def main():
	"""Puts together all that is needed to complete a drawing."""
	# draw_path(path = "M 0 0 H 32 V 32 H 0 L 0 0")
	points=[
		Point(16,16),
		Point(-16,16),
		Point(16,-16),
		Point(0,0),
	]
	ble_connection.run(points)

if __name__ == "__main__":
    main()