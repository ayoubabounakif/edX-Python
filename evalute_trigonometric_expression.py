# Function that calculates y for an x given

from math import sin, cos
def calculate_y_1(x):
    y = sin(x) - cos(x) + sin(x) * cos(x)
    return y

print (calculate_y_1(10)) # Main program (Testing calculate_y_1)

# Function that calculates y for an x given

from math import cos, sqrt
def calculate_y_2(x):
    y = abs(x**3) + cos(sqrt(3*x))
    return y

print (calculate_y_2(5)) # Main program (Testing calculate_y_2)

# Function that finds the distance between two points and returns it.
# The distance between two points with x, y and z components can be calculated as:

from math import sqrt
def distance(a, b):
    x1, y1, z1 = a[0], a[1], a[2]
    x2, y2, z2 = b[0], b[1], b[2]
    distance = sqrt(((x2 - x1)**2) + ((y2 - y1)**2) + ((z2 - z1)**2))
    return distance

print (distance([2, 3, -5], [4, -3, 12])) # Main program (Testing distance)
