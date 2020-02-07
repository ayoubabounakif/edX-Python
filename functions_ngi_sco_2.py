#       2. Nothing goes in, something comes out.
''' A great example of a function that does not receive anything
but does return something is the following. '''

import random

def report_random():
    my_number = random.randint(20, 100)
    return my_number

# Main Program #
a = report_random()    # return a random int and assign it to a
print("a is equal to ", a)

b = report_random()    # return a random int and assign it to b
print("b is equal to ", b)

c = report_random()    # return a random int and assign it to c
print("c is equal to ", c)

''' Notice that this function does not receive any arguments but each
time we call this function it returns a random integer between 20 and
100 and assigns the returned value to the variable the function call
was set equal to. '''

