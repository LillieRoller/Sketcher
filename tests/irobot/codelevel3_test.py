
from sketcher.irobot.codelevel3 import move, navigate_to

def test_move():
	expected = "await robot.move(16)"
	actual = move(16)
	assert expected == actual

def test_navigate_to():
	expected = "await robot.navigate_to(15,15)"
	actual = navigate_to(15, 15)
	assert expected == actual

def set_marker():
	expected = "await robot.set_marker()"
	actual = set_marker(UP)
	assert expected == actual