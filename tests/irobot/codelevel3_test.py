
from sketcher.irobot.codelevel3 import move, navigate_to, set_marker, Marker

def test_move():
	expected = "await robot.move(16)"
	actual = move(16)
	assert expected == actual

def test_navigate_to():
	expected = "await robot.navigate_to(15,15)"
	actual = navigate_to(15, 15)
	assert expected == actual

def test_set_marker_up():
	expected = "await robot.set_marker(Marker.UP)"
	actual = set_marker(Marker.UP)
	assert expected == actual

def test_set_marker_down():
	expected = "await robot.set_marker(Marker.DOWN)"
	actual = set_marker(Marker.DOWN)
	assert expected == actual