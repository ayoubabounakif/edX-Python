#           NOTES ON FUNCTIONS
# Most of the time we provide some arguments to a function and it returns something.
# However, this may not always be the case.
# While trying to write a function we need to decide
# if the function needs any arguments or not &
# if the function needs to return something or not.
# Broadly, we can attempt to classify the combination of
# function parameters and their return types as follows:

            # 1. Nothing goes in, nothing comes out. (CODE)
''' Sometimes we need to do some task repeatedly and that task never changes.
In this case, the function does not need any arguments (parameters)
and it does not need to return anything. '''

def display_message():
    print("****   PYTHON IS GREAT   ****")
    print("=============================")
    
# Main Program #
radius = 5
print("The radius of the circle is: ", radius)
display_message()    # The function call 

circumference = 2*3.14*radius
print("The circumference of the circle is:", circumference)
display_message()    # The function call

''' Note that the parentheses in the function call do not have any
anything which means the function does not take any arguments.
Also nothing is set equal to the function i.e. the function call is on a line by itself
which means it does not need to return anything.
So basically, this function just keeps printing the same message every time it is called
(Printing something is not the same as returning something).
Even though, there is no return keyword in this function,
it returns a None by default. '''




