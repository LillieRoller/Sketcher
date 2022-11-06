"""
Matches the commands at https://code.irobot.com/ to practice commands in the online simulator. 
Allows testing of programs by printing out the commands in output and copying them in the simulator.

All values are in centimeters.
"""

def move(cm:int)->str:
	"""Moves forward the number of centimeters given."""
	return f"await robot.move({cm})"

# define a function to move forward a certain distance