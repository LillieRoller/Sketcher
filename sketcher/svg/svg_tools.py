# Coordinates are given as points in the complex plane
from svgpathtools import Path, Line, QuadraticBezier, CubicBezier, Arc
seg1 = CubicBezier(300+100j, 100+100j, 200+200j, 200+300j)  # A cubic beginning at (300, 100) and ending at (200, 300)
seg2 = Line(200+300j, 250+350j)  # A line beginning at (200, 300) and ending at (250, 350)
path = Path(seg1, seg2)  # A path traversing the cubic and then the line

# We could alternatively created this Path object using a d-string
from svgpathtools import parse_path
path_alt = parse_path('M 10 10 H 90 V 90 H 10 L 10 10')

# Let's check that these two methods are equivalent
print(path)
print(path_alt)
print(path == path_alt)

# On a related note, the Path.d() method returns a Path object's d-string
print(path.d())
print(parse_path(path.d()) == path)