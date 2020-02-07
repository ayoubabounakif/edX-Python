# Function that accepts two lists both of which consists of integers and
# returns the total sum of all the odd integers from both lists.

#       CODE

def adding_odds_of_2_lists(list_1, list_2):
    new_list = []
    a = new_list
    for i in list_1:
        if i % 2 != 0:
            new_list.append(i)
    for i in list_2:
        if i % 2 != 0:
            new_list.append(i)
    new_list = sum(new_list)
    return new_list

print (adding_odds_of_2_lists([13,8,124,22,19], [1,9,23,10,22]))
    
            
    
