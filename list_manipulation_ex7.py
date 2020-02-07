# Function that accepts a list that contains positive integers
# and returns a new list which contains all the elements from original list
# but adds 1 to those elements which are odd.

#       CODE

def modify_list(list):
    new_list = list[:]
    for i in range(0, len(new_list)):
        if new_list[i] % 2 != 0:
            new_list[i] = new_list[i] + 1
    return new_list

print (modify_list([12, 3, 4, 5, 6]))

