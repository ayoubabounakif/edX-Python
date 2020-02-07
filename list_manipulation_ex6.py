# A function that accepts a list and return a new list which contains
# all but the first and last elements of the original list.

#       CODE

def extract_list(list):
    list.pop(0)
    list.pop(-1)
    return list

print (extract_list(['2', 'nine', 'seven', 'wrong!']))


    
