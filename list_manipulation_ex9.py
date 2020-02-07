# Function that accepts an input list and returns a new list which contains
# only the unique elements (Elements should only appear one time in the list
# and the order of the elements must be preserved as the original list).

#   CODE

def unique_list(list):
    new_list = []
    for items in list:
        if items not in new_list:
            new_list.append(items)
    return new_list

print (unique_list([3, 4, -5, 1, 1, 4]))

