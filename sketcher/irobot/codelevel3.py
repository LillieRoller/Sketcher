"""
Matches the commands at https://code.irobot.com/ to practice commands in the online simulator. 
Allows testing of programs by printing out the commands in output and copying them in the simulator.

All values are in centimeters.
"""

def move(cm:int)->str:
	"""Moves forward the number of centimeters given."""
	return f"await robot.move({cm})"

def navigate_to(x,y:int)->str:
	"""Navigates to the coordinants given"""
	return f"await robot.navigate_to({x},{y})"

def set_marker(Marker)->str:
	"""Sets the marker to either up or down"""
	Marker.UP = True
	Marker.DOWN = False
	return f"await robot.set_marker({Marker})"