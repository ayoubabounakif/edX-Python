###### MY CODE ######
def even_numbers(a, b):
    sum = 0
    even = []
    for i in a:
        if i % 2 == 0:
            even.append(i)  
            sum = sum + i
    for j in b:
        if j % 2 == 0:
            even.append(j)
            sum = sum + j
    return sum

###### INSTRUCTOR CODE ######
def sum_of_evens_edx(a, b):
    total_sum = 0
    for items in a:
        if items % 2 == 0:
            total_sum = total_sum + items
    for items in b:
        if items % 2 == 0:
            total_sum = total_sum + items
    return total_sum
        


