# A function that accepts two input lists and returns a new list which contains
# only the unique elements from both lists.

#   CODE

def unique_from_two_lists(list_1, list_2):
    new_list = []
    for items in list_1:
        if items not in new_list:
            new_list.append(items)
    for items in list_2:
        if items not in new_list:
            new_list.append(items)
    return new_list

print (unique_from_two_lists([3, 4, -5, 1], [1, 3, 4, 5, 7]))
