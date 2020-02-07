def largest_number(lst):
    max_value = lst[0]
    for i in lst:
        if i > max_value:
            max_value = i
    return max_value

print (largest_number([1, 2, 3, 4, -8]))
