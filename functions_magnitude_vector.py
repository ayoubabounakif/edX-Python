# Function that finds the magnitude of a given 3-dimensional vector.
# The magnitude of a vector is the sqrt of sum of squares of all the components
# of the vector
# magnitude = sqrt(x**2 + y**2 + z**2)
# The input for this function will be a (vector with x, y,z components) a list
# containing 3 integers i.e, [x, y, z].
# input list --> vector = [2, 3, -4]
# Return the magnitude (as a floating point number) of this vector
# 5.385164807134504



#       CODE 1

from math import sqrt

def magnitude_3d_vector(x, y, z):
    magnitude = sqrt(abs(x**2) + abs(y**2) + abs(z**2))
    return magnitude

print (magnitude_3d_vector(1,2,3))


#       CODE 2

def _magnitude_of_a_vector_sample_(vector):
    x = vector[0]
    y = vector[1]
    z = vector[2]
    mag = ((x**2) + (y**2) + (z**2))**(1/2)
    return mag
