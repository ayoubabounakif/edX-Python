# A function that normalizes a vector (finds the unit vector).
# A vector can be normalized by dividing each individual component
# of the vector by its magnitude.
# Your input for this function will be a vector i.e 1 dimensional list
# containing 3 integers. For example, if the input list is
# vector = [2, 3, -4]
# return the unit vector (1-D list) such as:
# [0.3713906763541037, 0.5570860145311556, -0.7427813527082074]

def normalize_vector(vector):
    x = vector[0] 
    y = vector[1] 
    z = vector[2]
    mag = ((x**2) + (y**2) + (z**2))**(1/2)
    new_x = x / mag
    new_y = y / mag
    new_z = z / mag
    vec_1d = [new_x, new_y, new_z]
    return vec_1d

print (normalize_vector([2,3,-4]))




    
