# Calculated the square root using a function

import math

def square_root(input_number):
    sqrt = math.sqrt(input_number)
    return sqrt

for k in range (1,999):
    y =  square_root(k)
    print ("Square root of",k, "is", y)
