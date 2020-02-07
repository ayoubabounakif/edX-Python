#       3. Something goes in, nothing comes out.
''' In this scenario, the function needs some arguments to do some task
but it does not need to return anything. '''

def calculate_area(length, breadth):
    area = length * breadth
    perimeter = 2*length + 2*breadth
    print("area is equal to", area)
    print("perimeter is equal to", perimeter)

# Main Program #
calculate_area(10, 20)

''' Notice that this function does receive two arguments length and
breadth and when we call this function, it calculates the area and
perimeter of a rectangle and prints the results but it does not return
anything! And again printing something is not the same as returning
some value. The return value once again for this function is None as
there is no return keyword. '''
