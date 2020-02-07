# A function that accepts a list and a value of an element and returns the count
# of how many times that element appears in the list.
# The behaviour of this function should be exactly like the list.count() method.
# You may NOT use any build in list methods for this problem.

#        CODE

def count_list(list, value):
    my_count = 0
    for element in list:
        if element == value:
            my_count = my_count + 1
    return my_count


print (count_list([2, 4, 4, 4, 4, 4, 4 , 6, 8], 4))
print (count_list(['hello', 22, 333, 3, 'hello', 4, 5, 6], 'hello'))
print (count_list([11, 2, 3, 11, 3, 14, 5, 6], 11))

