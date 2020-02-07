# A function that accepts two lists both of which contain integers and returns
# a new list which contains all the elements from both lists sorted
# in descending order
# Your new list should include duplicate elements if they exist.
# Do NOT use the build in sort() or sorted() methods.

#       CODE

def sorted_list(list_1, list_2):
    new_list = []
    extended_list = list_1 + list_2

    for i in range(len(extended_list)):
        new_list.append(max(extended_list))
        extended_list.remove(max(extended_list))
    return new_list

print (sorted_list([1, 1, 2, 4, 5], [0, 2, 5, 1]))









