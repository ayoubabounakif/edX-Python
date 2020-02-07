# Lets sort the following list by the first item in each sub-list. 
my_list = [[2, 4], [0, 13], [11, 14], [-14, 12], [100, 3]]

# First, we need to define a function that specifies what we would like our items sorted by
def my_key(item):
    return item[0]                                      # Make the first item in each sub-list our key

new_sorted_list = sorted(my_list, key=my_key)           # Return a sorted list as specified by our key
print("The sorted list looks like:", new_sorted_list)       
