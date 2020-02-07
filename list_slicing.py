# Single indexing (Replacing)

my_list = ['hello', 2.3, 8, 4.5, 'cat']
my_list[3] = 'dog'

print(my_list)

# Slicing --> list_name[start_index:end_index]

my_list = ['hello', 2.3, 8, 'dog', 'cat']
new_list = my_list[1:3]

print(new_list)

''' # Slicing begins at the start_index but it only goes to end_index - 1.
# In other words the end_index will not be included in the result. '''

# Negative Slicing

my_list = ['hello', 2.3, 8, 4.5, 'cat']
new_list_1 = my_list[0:-2]
new_list_2 = my_list[-3: -1]

print(new_list_1)
print(new_list_2)

# Slicing with a step
my_list = ['hello', 2.3, 8, 'dog', 'cat']
new_list_1 = my_list[0:4:2] 
new_list_2 = my_list[0:4:3]

print(my_list)
print(new_list_1)
print(new_list_2)

# Default Indexes

''' # if any of the indexes are missing in the slicing, then the default
# value for that index will be used: -> list_name[start_index:end_index:step]
# if the start_index is missing then it is assumed to be 0 (start of the list)
# if the end_index is missing then select to the end of the list (including the last element)
# if the step is missing then it is assured to be 1 '''

my_list = ['hello', 2.3, 8, 'dog', 'cat']
new_list_1 = my_list[:4]
new_list_2 = my_list[2:]
new_list_3 = my_list[2:4:]
new_list_4 = my_list[:]

print(my_list)
print(new_list_1)
print(new_list_2)
print(new_list_3)
print(new_list_4)




