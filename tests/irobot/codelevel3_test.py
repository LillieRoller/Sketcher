
from sketcher.irobot.codelevel3 import move

def test_move():
	expected="await robot.move(16)"
	actual = move(16)
	assert expected == actual
