# A function that accepts two lists A and B and returns a new list which
# contains all the elements of a list A followed by elements of list B.
# Notice that the behaviour of this function is different from list.extend()
# method because the list.extend() method extends the list in place,
# but here you are asked to create a new list and return it.
# Your function should not return the original lists.

def list_change(A, B):
    new_list = A.extend(B)
    return new_list

def list_manipulation(A, B):
    # In Python we can implement out version of list.extend
    # using the '+' operator
    new_list = A + B
    return new_list

print (list_change(["1", "2", "3"], ["4", "5"]))
print (list_manipulation(["1", "2", "3"], ["4", "5"]))



