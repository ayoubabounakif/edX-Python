#       4. Something goes in, something comes out.
''' This is probably the most meaningful scenario where the function
takes some arguments and performs some task using those
arguments and returns some result as well. '''

def calculate_area(length, breadth):
    area = length * breadth
    perimeter = 2*length + 2*breadth
    my_result = [area, perimeter]    # put results in a list
    return my_result                 # return the list

# Main Program #
my_list = calculate_area(10, 20) # two arguments are supplied 
print("The resulting list looks like:", my_list)

''' Note that we can return multiple things in python by separating them
with a comma. For example instead of returning the results in a list
we could have done the following: --> ''' #return area, perimeter

                                        
