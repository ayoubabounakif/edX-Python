# A function that accepts a list and returns a new list such that
# the new list contains all the items of the old list in reverse order.
# Note that this is NOT a sorting problem.
# Do NOT use the build in reverse() method for this problem.

#       CODE

def traverse_backwards_list(list):
    reversed_list = []
    for x in list:
        reversed_list = list[::-1]
    return reversed_list

print (traverse_backwards_list([0,10,20,40,50,60,70,80,90,100]))
