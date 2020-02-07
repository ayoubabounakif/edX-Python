# A function that accepts a list of integers and returns a new list which is the
# sorted version (ascending order) of the original list (Original list should not
# be modified). You may NOT use the build in sort() or sorted() functions.
# Notice that the original list should not be modified.

#       CODE

def sorted_list(list):
    new_list = []
    for i in range(len(list)):
        new_list.append(min(list))
        list.remove(min(list))
    return new_list

print (sorted_list([64, 25, 12, 22, 11, 1, 2, 44, 3, 122, 23, 34]))
