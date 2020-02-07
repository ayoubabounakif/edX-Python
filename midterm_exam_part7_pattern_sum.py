###### MY CODE ######
def pattern_sum(a, b):
    c = 0
    sum = 0
    for n in range(1, b+1):
        pattern = a * ((10**n)/10) + c
        c = pattern
        print (pattern)
        sum = sum + c
    return int(sum)

print (pattern_sum(5, 3))


###### INSTRUCTOR CODE ######
def chain_of_number_sample_edx(a, b):
    chain_list = []
    my_sum = 0
    for x in range(1, b+1):
        chain_list.append(x*str(a))
        print (chain_list)
    for items in chain_list:
        my_sum = my_sum + int(items)

    return my_sum

print (chain_of_number_sample_edx(5, 3))




